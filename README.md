# insolent-chainsaw
Pobierz dane z Overpass API, skonwertuj do PBF i wystaw w miejsce publiczne

## Extract
Sposób wywołania
./extract.py obszar polecenie

Obszary zdefiniowane są w pliku konfig.py
polecenie może przyjąć dwie wartości:
* sql -> spowoduje uruchomienie procesu imposma
* www -> spowoduje skopiowanie do katalogu serwera www i udostępnienie adresu do pliku
* process -> przetwarzanie pobranego pliku pbf
Wartość dla polecenia jest obowiązkowa!


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
* usage()
  Drukowanie informacji o sposovie uruchomienia

## Konfiguracja (konfig.py)

* mapping_f - plik mappingu Imposma
* osmconvert_dir - ścieżka dostępu do katalogu binariów osmosis
* imposm_dir - ścieżka dostępu do katalogu binariów Imposm3
* www_dir - ścieżka dostępu do katalogu www
* baza - adres bazowy usługi overpass
* obszar - definicje obszarów (bbox) dla ekstraktów. Przykładowa definicja poniżej
        'swiebodzin':
          {'name': 'Powiat Świebodziński',
           'bbox':'14.92,52,15.94,52.5'
          }
