#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pycurl
from datetime import datetime
from konfig import *
from funkcje import *
from subprocess import (PIPE, Popen)

extract_key = sys.argv[1]
wykonaj = sys.argv[2]

try:
    bbox = obszar.get(extract_key,{}).get('bbox')
    name = obszar.get(extract_key,{}).get('name')
    pobierz = baza + bbox
    xml_name = extract_key + '.osm'
    pbf_name = extract_key + '.osm.pbf'
    pbf_dest = imposm_dir + pbf_name
except TypeError:
    usage()
    print "Zdefiniowane obszary:"
    for item in obszar:
        print item
    sys.exit()

def get_osm(plik):
    '''
    Pobierz wybrany fragment danych OSM na podstawie zdefiniowanego bbox
    '''
    c = pycurl.Curl()
    c.setopt(c.URL, pobierz)
    c.setopt(c.HTTPHEADER, ['Connection: Keep-Alive','Keep-Alive: 1000'])
    try:
        with open(plik, 'wb') as f:
            c.setopt(c.WRITEDATA, f)
            c.perform()
            c.close()
            print 'Zapisano XML'
    except pycurl.error:
        print "Błąd komunikacji sieciowej. Sprawdź połączenie internetowe"
        sys.exit()

def to_pbf(xml,pbf_f):
    '''
    Przetwórz .OSM.XML do .pbf
    Parametry:  xml - plik xml pobrany z api Overpass
                pbf - plik do wygenerowania
    '''
    p_osmc = osmconvert_dir + 'osmconvert '+ xml +' -o='+ pbf_f
    try:
        o_result = run(p_osmc)
        print 'Osmconvert skończył pracę'
    except IOError:
        print "Zepsułem coś w Osmconvert. Błąd I/O. Sprawdź uprawnienia zapisu"
        sys.exit()

def to_sql(mapping, pbf_f):
    '''
    Wykonaj import do bazy
    Parametry:  mapping - ścieżka dostępu do pliku mappingu imposma
                pbf_f - ścieżka dostępu do pliku źródłowego pbf_f
    '''
    p_imposm = imposm_dir + 'imposm3 import -mapping '+ mapping +' -connection postgis://osm:osm@localhost:5432/osm -read '+ pbf_f +' -write -overwritecache'
    try:
        i_result = run(p_imposm)
        print i_result
        print 'Imposm3 skończył pracę'
    except:
        print "Zepsułem coś w Imposm. Sprawdź ścieżki dostępu i mapping"
        sys.exit()

def to_url(pbf_f, pbf_n, www_dir):
    '''
    Skopiuj plik do przestrzeni serwera www
    Parametry:
        pbf_f - ściezka dostepu do pliku pbf
        pbf_n - nazwa pliku pbf
        www_dir - katalog serwera www
    '''
    try:
        cmd = 'cp '+ pbf_f + ' ' + www_dir
        url_copy_result = run(cmd)
        www_pth = www_dir + pbf_n
        os.chmod(www_pth, 0666)
    except IOError:
        print "Błąd I/O. Sprawdź uprawnienia zapisu i ścieżki dostępu"
        print "Wykonywano: " + cmd
        sys.exit()

get_osm(xml_name)
to_pbf(xml_name, pbf_dest)
if wykonaj == 'sql':
    to_sql(mapping_f, pbf_dest)
else:
    to_url(pbf_dest, pbf_name, www_dir)
    url_uri = 'http://et21.gis-support.pl/' + pbf_name
with open('metadata.txt', 'a') as l:
    timestamp = datetime.now()
    msg_meta = name + '\n "' + bbox + '"\n    ' + str(timestamp) + '\n'
    l.write(msg_meta)
    l.close()
xml_size = filesizemb(xml_name)
pbf_size = filesizemb(pbf_dest)
xml_msg = 'XML: ('+ str(xml_size) +'MB)'
pbf_msg = 'PBF: ('+ str(pbf_size) +'MB)'
msg_sizes = xml_msg + ' ' + pbf_msg
if wykonaj != 'sql':
    print url_uri
print msg_meta
print msg_sizes
