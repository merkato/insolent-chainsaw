#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pycurl
from datetime import datetime
from konfig import *
from funkcje import *
from subprocess import (PIPE, Popen)

#Inicjalizacja zmiennych
extract_key = sys.argv[1]
bbox = obszar.get(extract_key,{}).get('bbox')
name = obszar.get(extract_key,{}).get('name')
pobieracz = baza + bbox
xml_name = extract_key + '.osm'
pbf_name = extract_key + '.osm.pbf'
pbf_dest = imposm_dir + pbf_name

def get_osm(plik):
    '''
    Pobierz wybrany fragment danych OSM na podstawie zdefiniowanego bbox
    '''
    with open(plik, 'wb') as f:
        c = pycurl.Curl()
        c.setopt(c.URL, pobieracz)
        c.setopt(c.HTTPHEADER, ['Connection: Keep-Alive','Keep-Alive: 1000'])
        c.setopt(c.WRITEDATA, f)
        c.perform()
        c.close()

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
    except:
        pass

def to_sql(mapping, pbf_f):
    '''
    Wykonaj import do bazy
    Parametry:  mapping - ścieżka dostępu do pliku mappingu imposma
                pbf_f - ścieżka dostępu do pliku źródłowego pbf_f
    '''
    p_imposm = imposm_dir + 'imposm3 import -mapping '+ mapping +' -connection postgis://osm:osm@localhost:5432/osm -read '+ pbf_f +' -write -overwritecache'
    try:
        i_result = run(p_imposm)
    except:
        pass

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
    except:
        pass
    return url_uri

with open('metadata.txt', 'a') as l:
    get_osm(xml_name)
    to_pbf(xml_name, pbf_dest)
    to_sql(mapping_f, pbf_dest)
    url_uri = to_url(pbf_dest, pbf_name, www_dir)
    xml_size = filesizemb(xml_name)
    pbf_size = filesizemb(pbf_dest)
    kompresja = xml_size / pbf_size
    xml_msg = 'XML: ('+ str(xml_size) +'MB)'
    pbf_msg = 'PBF: ('+ str(pbf_size) +'MB)'
    kompresja_msg = 'R: '+ str(int(kompresja)) +'%'
    timestamp = datetime.now()
    msg = name + '\n "' + bbox + '"\n    ' + str(timestamp) + '\n'
    msg_sizes = xml_msg + ' ' + pbf_msg + kompresja_msg
    print '\n'
    print msg
    print url_uri
    print msg_sizes
    l.write(msg)
    l.close()
