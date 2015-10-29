#!/usr/bin/python
# -*- coding: utf-8 -*-

# Definicje lokalne
mapping_f = '/home/mechanik/dev/imposm3/topo.json'
osmconvert_dir = '/home/mechanik/dev/osmconvert/'
imposm_dir = '/home/mechanik/dev/imposm3/'
www_dir = '/home/mechanik/www/'

#Definicje instalacja dev
#osmconvert_dir = '/home/f_janecek/osmconvert/'
#imposm_dir = '/home/f_janecek/pbfs/'
#www_dir = '/home/f_janecek/www/'

#Adres URL serwera API Overpass
baza = 'http://www.overpass-api.de/api/xapi?map?bbox='

#Definicje obszarów
obszar = {
        'przemysl': {'name': 'Miasto Przemyśl', 'bbox': '22.62,49.69,22.98,49.87'},
        'swd':  {'name': 'Powiat Wodzisławski', 'bbox':'18.194,49.82,18.634,50.11'},
        'slezsko': {'name': 'Morawskośląskie międzygórze', 'bbox':'17.8,49.50,19.50,52'},
        'chojnice': {'name': 'Powiat Chojnicki', 'bbox':'16.8,53.45,18.3,54.05'},
        'olesno': {'name': 'Olesno i okolice', 'bbox':'18.30,50.70,18.68,51.05'},
        'swiebodzin': {'name': 'Powiat Świebodziński', 'bbox':'14.92,52,15.94,52.5'},
        'test': {'name': 'Unit Test', 'bbox':'17.95605,50.1019,17.97759,50.11577'},
        'bbi': {'name': 'My Zza Buga', 'bbox':'22.31,52.77,24.10,53.79'},
        'ppz': {'name': 'Poznań-Zadupie', 'bbox':'16.40,52.07,17.49,52.764'},
        'fza': {'name': 'Powiat Żarski', 'bbox': '14.55,51.33,15.35,51.92'},
        'istebna': {'name': 'Istebna', 'bbox': '18.80585,49.50827,18.983,49.61516'},
        'rro': {'name': 'Ropczyce', 'bbox': '21.41,49.84,21.90,50.24'},
        'ksiestwo': {'name': 'Autonomiczna Republika Górno-Koniakowska', 'bbox':'15.60,48.60,20.70,51.37'}
        }
