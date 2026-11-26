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
        
        lokalizacja = lista[7]
        if lokalizacja not in pojazdy:
            pojazdy[lokalizacja] = {}


        if pojazd not in pojazdy[lokalizacja]:
            pojazdy[lokalizacja][pojazd] = [0,0]

        cena_obl = pojazdy[lokalizacja] [ pojazd ][0]+cena
        liczba_obl = pojazdy[lokalizacja][pojazd][1] + 1
        pojazdy[lokalizacja][pojazd] = [cena_obl,liczba_obl]

print(f"Pojazdow jest {ile_total}, cena razem: {suma_total}")
# print(pojazdy)

#tab=pt(["pojazd", "Cena","Ilosc", "Srednia"])

for lokalizacja, x in pojazdy.items():
    #print(lokalizacja)
    tab=pt(["pojazd", "Cena","Ilosc", "Srednia"])

    for pojazd, y in x.items():
        ceny = f"{y[0]:_.0f}".replace("_"," ")
        ile = y[1]
        srednia=  round(  y[0]/y[1] ,1)
        tab.add_row([pojazd,ceny,ile, srednia])




    with open("dane\\" + lokalizacja + ".txt","w",encoding="utf-8", newline="") as plik:
        plik.write(tab.get_string())
        plik.write("\n\n")
        plik.write(tab.get_csv_string(delimiter=";"))

czas_koniec = time.time()
ile_trwalo = f"{czas_koniec-czas_start:.2f} s"

print(f"Czas: {ile_trwalo}")