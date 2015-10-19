#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pycurl
from datetime import datetime
from konfig import *
from funkcje import *
from subprocess import (PIPE, Popen)

extract_key = sys.argv[1]
try:
    bbox = obszar.get(extract_key,{}).get('bbox')
    name = obszar.get(extract_key,{}).get('name')
    pobieracz = baza + bbox
    xml_name = extract_key + '.osm'
    pbf_name = extract_key + '.osm.pbf'
    pbf_dest = imposm_dir + pbf_name
except TypeError:
    print "Niepoprawny argument obszaru.\n"
    print "Poprawna składnia: ./extract_full.py obszar"
    print "Zdefiniowane obszary:"
    for item in obszar:
        print item
    sys.exit()

def get_osm(plik):
    '''
    Pobierz wybrany fragment danych OSM na podstawie zdefiniowanego bbox
    '''
    c = pycurl.Curl()
    c.setopt(c.URL, pobieracz)
    c.setopt(c.HTTPHEADER, ['Connection: Keep-Alive','Keep-Alive: 1000'])
    try:
        with open(plik, 'wb') as f:
            c.setopt(c.WRITEDATA, f)
            c.perform()
            c.close()
    except pycurl.error:
        print "Błąd komunikacji sieciowej. Sprawdź połączenie internetowe"
        sys.exit()

def to_pbf(xml,pbf_f):
    '''
    Przetwórz .OSM.XML do .pbf
    Parametry:  xml - plik xml pobrany z api Overpass
                pbf - plik do wygenerowania
    '''
    p_osmosis = osmosis_dir+ 'osmosis --read-xml file='+ xml +' \
    --write-pbf file='+ pbf_f +' omitmetadata=true granularity=1000'
    try:
        o_result = run(p_osmosis)
    except IOError:
        print "Błąd I/O. Sprawdź uprawnienia zapisu"
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
        url_uri = 'http://dev.gis-support.pl/repo/pbfs/' + pbf_n
    except IOError:
        print "Błąd I/O. Sprawdź uprawnienia zapisu i ścieżki dostępu"
        print "Wykonywano: " + cmd
        sys.exit()
    return url_uri

with open('metadata.txt', 'a') as l:
    get_osm(xml_name)
    to_pbf(xml_name, pbf_dest)
    url_uri = to_url(pbf_dest, pbf_name, www_dir)
    xml_size = filesizemb(xml_name)
    pbf_size = filesizemb(pbf_dest)
    xml_msg = 'XML: ('+ str(xml_size) +'MB)'
    pbf_msg = 'PBF: ('+ str(pbf_size) +'MB)'
    timestamp = datetime.now()
    msg = name + '\n "' + bbox + '"\n    ' + str(timestamp) + '\n'
    msg_sizes = xml_msg + ' ' + pbf_msg
    print '\n'
    print msg
    print url_uri
    print msg_sizes
    l.write(msg)
    l.close()
