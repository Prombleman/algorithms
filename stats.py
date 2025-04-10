'''
Wykonaj podstawowe obliczenia statystyczne (ile, suma, średnia,
mediana, moda) na liczba z pliku dane.txt.
Wykonaj wykres kolumny ilości wystąpień liczb w pliku.
'''
import sys
import statistics
import matplotlib.pyplot as plt

def f_wystapienia(liczby):
    wystapienia = {}
    for i in liczby:
        if i not in wystapienia:
            wystapienia[i] = 1
        else:
            wystapienia[i] += 1
    return wystapienia



def moda(liczby):
    wystapienia = f_wystapienia(liczby)
    maks = -99999999999999999999
    for i in wystapienia.keys():
        if maks < wystapienia[i]:
            maks = wystapienia[i]
    mody = []
    for k,v in wystapienia.items():
        if v == maks:
            mody.append(k)
    if len(mody) == len(wystapienia.keys()):
        mody.clear()   
    return  mody



def mdp(liczby): #dla parzystej ilości liczb
    dl = len(liczby)
    return (liczby [int(dl/2)-1] + liczby[int(dl/2)]) / 2

def mdn(liczby): #dla nieparzystej ilości liczb
    dl = len(liczby)
    return liczby [int(dl/2)]
       

def bubble(liczby):
    for i in range(len(liczby)):
        for j in range(len(liczby)-1):
            if liczby[j] > liczby[j+1]:
                liczby[j],liczby[j+1] = liczby[j+1],liczby[j]
    return liczby

def wyczytaj(nazwa):
    try:
        file = open (nazwa, 'r')
        line = file.readlines()
        liczby = [int(i.replace("\n","")) for i in line ]
        file.close()
        return liczby
    except IOError as e:
        print(f"Problem z plikiem {e.errno} : {e.strerror}")
    except:
        print(f"Nieoczekiwany błąd pliku. {sys.exc_info()[0]}")
        raise
    finally:
        print("Skończyłem wczytywanie pliku.")

def staty(liczby):
    n = len(liczby)
    print(f"\nLiczb w pliku jest: {n}")

    suma = sum(liczby)
    print(f"Suma liczb to: {suma}")

    suma2 = 0
    for i in range(n):
        suma2 += liczby[i] 
    print(f"Suma liczb (petla) to: {suma2}") 

    srednia = statistics.mean(liczby)
    print(f"Średnia to: {srednia}")

    srednia2 = float(suma / n)
    print(f"Średnia obliczona: {srednia2}")

    
    liczby_posortowane = bubble(liczby)
    print((f"Mediana wynosi: {mdp(liczby_posortowane)}") if len(liczby) % 2 == 0 else f"Mediana wynosi: {mdn(liczby_posortowane)}")
    
    print(liczby)
    if len(moda(liczby))==0:
        print("Brak mody")
    else:
        maks = moda(liczby)
        print(f"Moda:{maks}")


    wys = f_wystapienia(liczby)
    wys_posortowany = dict(sorted(wys.items()))
    x, y = wys_posortowany.keys(), wys_posortowany.values()
    min_v,max_v = min(y), max(y)



    print(f"Minimalna {min_v}, maksymalna {max_v}")
    
    krok = 1
    if n > 1000:
        krok = 10
    elif n > 100000:
        krok = 100


    os_y = [i for i in range(1,max_v + 1 ,krok)]

    if len(liczby)%2 == 0:
        ned = mdp(liczby_posortowane)
    else:
        ned = mdn(liczby_posortowane)
    print(f"Mediiana wynosi: {ned}")


    # plt.figure(figsize = (10,10))
    # plt.bar(x,y)
    # plt.title(f"Wykres częstości westąpień ze zbioru {n} liczb \n najczęściej liczby wstępują  {maks} razy | średnia to {srednia} | mediana wynosi {ned}")
    # plt.xlabel("Liczba")
    # plt.ylabel("Ilość wystąpień")
    # plt.yticks(os_y)
    # plt.show()




#Co się stanie,jak będzie równa ilość liczb(nie ma mody)


# =================================== Start programu 
nazwa = input("Podaj nazwe pliku wraz z rozszerzeniem: ")
liczby = wyczytaj(nazwa)
print(f"Pracujemy na liczbach: {liczby}")

staty(liczby)
