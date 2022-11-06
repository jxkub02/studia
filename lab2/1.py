print('''Zadanie 1 (1.py):
• Dla osób poniżej 4 roku życia wstęp jest bezpłatny.
• Dla osób w wieku od 4 do 18 lat bilet kosztuje 10zł.
• Dla osób powyżej 18 roku życia bilet kosztuje 20zł.
Przykład: Wprowadź wiek klienta: 5
Cena biletu: 10zł

zad 1
age = int(input("podaj wiek: "))

if age < 4:
    price = 0
elif age < 18:
    price = 10
else:
    price = 20

print("cena biletu: ")


zad 3
Napisz skrypt działający jak prosty kalkulator, który potrafi dodawać, odejmować, mnożyć,
dzielić oraz obliczać potęgę.
Przykład: Jaką operację chcesz wykonać?
1) dodawanie
2) odejmowanie
3) mnożenie
4) dzielenie
5) potęgowanie
Wpisz numer operacji: 2
Podaj argument 1: 34
Podaj argument 2: 5
Wynik: 29

mode = int(input())
if mode > 5 or mode < 1:
    print("niepoprawne działanie")
    exit()

var1 = float(input("podaj var1: "))
var2 = float(input("podaj var2: "))

if mode == 1:
    wynik = var1+var2
    
elif mode == 2:
    wynik = var1-var2
    
elif mode == 3:
    wynik = var1*var2
    
elif mode == 4:
    if var2 == 0:
        print("nie mozesz dzielic przez 0")
        exit()
    wynik = var1/var2
    
elif mode == 5:
    wynik = var1**var2
    
pprint("wynik operacji", mode, "to", wynik)''')


