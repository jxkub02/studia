print('''zad 4
Zmodyfikuj program z zad. 1 tak, aby przechodząc po kolejnych liczbach przedziału, wypisywać
tylko liczby parzyste, a nieparzyste – pomijać. Użyj instrukcji continue.''')

a = int(input("liczba 1: "))
b = int(input("liczba 2: "))
print("wejscie", a,", ", b)
if a > b:
    (a,b)=(b,a)
while a <= b:
    if a % 2 == 1
        a += 1
        continue
    print(a, end=' ')
    a += 1