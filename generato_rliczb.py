'''
Generator liczb do pliku
'''

import random as rd 


n = int(input("Podaj ilość liczb: "))
jakie = input(("Jakie liczbe? [i - całkowite, r - rzeczewiste]"))

if jakie in ['i', 'r']:
    d = int(input("Podaj dolny zakres: "))
    g = int(input("Podaj górny zakres: "))

    if d>g:
        d,g = g,d

    nazwa = input("Podaj nazwe pliku: ")
    nazwa += ".txt"

    file = open(nazwa, "a")
    
    
    if jakie == 'i':
        for i in range(n):
            liczba = rd.randint(d,g)
            file.write(str(liczba)+str("\n"))
    elif jakie == 'r':
        for i in range(n):
            liczba = rd.uniform(d,g)
            file.write(str(liczba)+str("\n"))
    print(f"Wygenerowałem do pliku {nazwa}")
    file.close()
else:
    print("Miałeś podać r lub i...")

