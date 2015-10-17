# insolent-chainsaw
Pobierz dane z Overpass API, skonwertuj do PBF i wystaw w miejsce publiczne

## Extract/Extract_Full

Dostępne funkcje
* get_osm()
  Pobiera dane z serwera Overpass
* to_pbf()
  Konwersja do PBF
* to_sql()
  Uruchamianie imposma
* to_url()
  Kopiowanie do katalogu serwera WWW i udostępnienie adresu

## Funkcje (funkcje.py)

* run(cmd)
  Uruchamianie procesu zewnętrznego
* filesizemb(filepath)
  Obliczanie wielkości pliku na dysku

## Konfiguracja (konfig.py)

* mapping_f - plik mappingu Imposma
* osmosis_dir - ścieżka dostępu do katalogu binariów osmosis
* imposm_dir - ścieżka dostępu do katalogu binariów Imposm3
* www_dir - ścieżka dostępu do katalogu www
* baza - adres bazowy usługi overpass
* obszar - definicje obszarów (bbox) dla ekstraktów. Przykładowa definicja poniżej
        'swiebodzin':
          {'name': 'Powiat Świebodziński',
           'bbox':'14.92,52,15.94,52.5'
          }
