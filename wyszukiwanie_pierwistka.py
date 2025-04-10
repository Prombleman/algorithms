'''
Wyszukiwanie pierwistka kwadratowego 
metodą Newtona-Rapsona(zwykły pierwiastek z liczby)
'''

eps = float(input("Podaj eps: "))
n = int(input("Podaj liczbę pierwiastkowaną: "))


def pierw(n, eps):
    a =1 
    b = n
    while abs(a - b) >= eps:
        a = (a + b) / 2.0
        b = float(n / a)
    return (a + b) / 2.0

print(f"Pierwiastek z liczby n wynosi {pierw(n, eps)}")