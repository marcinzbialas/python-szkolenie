print("Czesc. Działamy")
# import cowsay
# cowsay.cow("Cześć")
# cowsay.dragon("Cześć")
# print(cowsay.char_names)
# """
# abcjskljdlksjl
# """
# print("tekst", "inny")
# print("tekst"+"inny")
# print("+++" * 4)
# x=3
# y=4
# print(x+y)
# abc = None
# wartość = 1
x,y,z=1,"Ala",2
print(x)
y=12
z=12.43
w=True
y="10.44"
xx=round(float(y)+z,2)
print(xx)
miasto="Łeba"
kiedy=15
kasa=1234.1234567
print(f"na wakacje pojade {kiedy} do {miasto}, wydam {kasa:_.2f} ")
ladnaliczba = f"{kasa:_.2f}".replace("_"," ")
print(f"Liczba: {ladnaliczba}")
print(2**4)
print(len(str(kasa)))
print(len(ladnaliczba))
print("01","10","2023",sep="-")
b="Hello, World"
print(b[2:5])
imie="bialas"
poprawione_imie=imie.upper()
print(poprawione_imie)
imie=imie.title().   \
replace("l","ł") # lamanie wierszy
print(imie)
tekst_CSV="03/22/2025 jan Kowalski wyplata PLN: 8359"
# tekst_CSV="03/22/2025 marek PIEKNY wyplata PLN: 10992.12"
print("data:", tekst_CSV[0:10])
wyplata=tekst_CSV.find("wyplata")
print("Imię i nazwisko:",tekst_CSV[11:wyplata].title())
wyplataPLN=tekst_CSV.find(":")
print("zarabia ", tekst_CSV[wyplataPLN:], "PLN")
zl=float(tekst_CSV[wyplataPLN+2:])
euro=4.33*zl
print("w Euro: ", euro)
print(f"{tekst_CSV[0:10]} {tekst_CSV[11:wyplata].title()}", euro)
from datetime import datetime, date, timedelta
teraz = datetime.now()
print(f"Teraz jest: {teraz}")
print("Teraz jest: ",teraz)
urodziny = date(1995,10,20)
print(f"Urodziny: {urodziny}")
przyszłosc=teraz + timedelta(days=100)
print(f"Za 100 dni będzie: {przyszłosc.date()}")
ladna_data=teraz.strftime("%d.%m.%Y %H:%M")
print(f"Format europejski: {ladna_data}")
data=tekst_CSV[0:10]
data_prawidlowa = datetime.strptime(data, "%m/%d/%Y")
print(data_prawidlowa)