from prettytable import PrettyTable as pt
from dane.dane_zdarzenia import zdarzenia
liczba_zdarzen=len(zdarzenia)
print(f"Całkowita liczba zdarzeń: {liczba_zdarzen}")

liczba_minor=0
liczba_serious=0

for zdarzenie in range(len(zdarzenia)):
    if zdarzenia[zdarzenie][3] == "minor":
        liczba_minor= liczba_minor+1
    if zdarzenia[zdarzenie][3] == "serious":
            liczba_serious= liczba_serious+1

po_lotnisku={}
po_typie={}

for data, icao, typ, powaga, samolot in zdarzenia
    if icao not in po_lotnisku:
         



print(f"Liczba zdarzeń 'minor': {liczba_minor}")
print(f"Liczba zdarzeń 'serious': {liczba_serious}")

