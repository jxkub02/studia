print('''zad 3
Napisz pętlę nieskończoną, w której użytkownik podaje liczby całkowite. W przypadku liczby
ujemnej, następuję wyjście z pętli.''')

while True:
    x = int(input("podaj liczbe całkowita: "))
    if x < 0:
        break
print("koniec")