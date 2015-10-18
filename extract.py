#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, pycurl
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
        paczka = str(int(c.getinfo(c.SIZE_DOWNLOAD)/1048576))
        speed = str(int(c.getinfo(c.SPEED_DOWNLOAD)/1024))
        c.close()
        return paczka, speed

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
    paczka, speed = get_osm(xml_name)
    to_pbf(xml_name, pbf_dest)
    url_uri = to_url(pbf_dest, pbf_name, www_dir)
    pbf_msg = ' ('+ str(filesizemb(pbf_dest)) +'MB) \n'
    timestamp = datetime.now()
    msg = name + ', "' + bbox + '"\n    ' + paczka + 'MB, ' + speed + 'kB/s :'+ str(timestamp) + '\n'
    print msg
    print url_uri
    print pbf_msg
    l.write(msg)
    l.close()
