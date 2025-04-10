'''
Szyfr Cezara
'''

def uruchom():
    klucz = 0


    odp = menu()
    if odp in ['s','d']:    
        if odp == 's':
            tekst = input("Podaj tekst do zaszyfrowania: ")
            klucz = pobierz_klucz()
            szyfruj(tekst, klucz)
        elif odp == 'd':
            tekst = input("Podaj tekst do deszyfrowania: ")
            klucz = pobierz_klucz()
            deszyfruj(tekst, klucz)
    else:
        print("ERROR...")

def pobierz_klucz():
    klucz = 0
    while klucz==0 and type(klucz)!='int':
        try:
            klucz = int(input("Podaj klicz (liczba): "))
        except ValueError:
            print("ERROR...")
    return klucz

def menu():
    print("="*40)
    print("="*13,"Szyfr cezara","="*13)
    print("="*40)
    print("Menu: s - szyfruj, d - deszyfruj")
    odp = input("Wybierz działanie: ")
    return odp

def szyfruj(tekst, klucz):
    print("Szyfriowanie...")
    print(f"Tekst do zaszyfrowania: \n{tekst}")
    print(f"Klucz:{klucz}")
    szyfr = ''
    for i in tekst:
        szyfr += chr(32+((int(ord(i)) + klucz - 32) % 94))
    print(f"\nTekst deszyfrowany:\n{szyfr}")

def deszyfruj(tekst, klucz):
    print("Deszyfriowanie...")
    print(f"Tekst do deszyfrowania: \n{tekst}")
    print(f"Klucz:{klucz}")
    odszyfr = ''
    for i in tekst:
        odszyfr += chr(32+((int(ord(i)) - klucz - 32) % 94))
    print(f"\nTekst deszyfrowany:\n{odszyfr}")

#=========================================
while True:

    uruchom()
    co = input("Kończymy? (t/n)")
    if co in ['t','n','T','N']:
        if co == 't' or co == 'T':
            print("Koniec pracy...")
            break
    else:
        co = input("Wybierz czy kończysz (t/n)...")



