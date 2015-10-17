#!/usr/bin/python
# -*- coding: utf-8 -*-

mapping_f = 'mapping_topo_c.json'
osmosis_dir = '/home/mechanik/dev/konwersje/osmosis-latest/bin/'
imposm_dir = '/home/mechanik/dev/imposm3/'
www_dir = '/home/mechanik/dev/pbfs'

#Adres URL serwera API Overpass
baza = 'http://www.overpass-api.de/api/xapi?map?bbox='

#Definicje obszarów
obszar = {
        'przemysl': {'name': 'Miasto Przemyśl', 'bbox': '22.62,49.69,22.98,49.87'},
        'swd':  {'name': 'Powiat Wodzisławski', 'bbox':'18.194,49.82,18.634,50.11'},
        'slezsko': {'name': 'Morawskośląskie międzygórze', 'bbox':'17.8,49.50,19.50,52'},
        'chojnice': {'name': 'Powiat Chojnicki', 'bbox':'16.8,53.45,18.3,54.05'},
        'olesno':{'name': 'Olesno i okolice', 'bbox':'18.30,50.70,18.68,51.05'},
        'swiebodzin':{'name': 'Powiat Świebodziński', 'bbox':'14.92,52,15.94,52.5'},
        'test':{'name': 'Unit Test', 'bbox':'17.95605,50.1019,17.97759,50.11577'}        
        }
17.95605,50.1019,17.97759,50.11577
