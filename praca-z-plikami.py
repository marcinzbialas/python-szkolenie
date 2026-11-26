from prettytable import PrettyTable as pt
import time

# plik = open(r"dane\moje-dane.txt","rt")
# zaw = plik.read()
# plik.close()

# # alternatywa

# with open(r"dane\moje-dane.txt","rt") as plik:
#     zaw = plik.read()

# print(zaw)

# # zapis

# with open(r"dane\moje-dane.txt","a") as plik:
#     plik.write("\najdgajhdgakg")

# importujemy samochody z pliku dane.csv
ile=0

suma_total=0
ile_total=0
pojazdy = {}

czas_start=time.time()

with open(r"dane\dane_2_mln.csv",encoding="utf-8") as plik:
    for wiersz in plik:
        if ile == 0:
            ile +=1
            continue
        else:    
            # print(wiersz.strip())
         # ile = ile+1
            ile += 1
            if ile == 100000000000:
                break
        
        lista = wiersz.split(";")
        # print(lista)
        pojazd = lista[1]
        cena = float(lista[2])
        # suma_total = suma_total + cena
        suma_total += cena
        ile_total += 1
        # uzupelnianie slownika
        
        if pojazd not in pojazdy:
            pojazdy[pojazd] = [0,0]

        cena_obl = pojazdy [ pojazd ][0]+cena
        liczba_obl = pojazdy[pojazd][1] + 1
        pojazdy[pojazd] = [cena_obl,liczba_obl]

print(f"Pojazdow jest {ile_total}, cena razem: {suma_total}")
# print(pojazdy)

tab=pt(["pojazd", "Cena","Ilosc", "Srednia"])

for pojazd, x in pojazdy.items():
    ceny = f"{x[0]:_.0f}".replace("_"," ")
    ile = x[1]
    srednia=  round(  x[0]/x[1] ,1)
    tab.add_row([pojazd,ceny,ile, srednia])

print(tab)


with open(r"dane\moje_dane.txt","w",encoding="utf-8", newline="") as plik:
    plik.write(tab.get_string())
    plik.write("\n\n")
    plik.write(tab.get_csv_string(delimiter=";"))

czas_koniec = time.time()
ile_trwalo = f"{czas_koniec-czas_start:.2f} s"

print(f"Czas: {ile_trwalo}")