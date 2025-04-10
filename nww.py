'''
Szukanie NWW
'''


def nwd(a,b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

def nww(a,b):
    return float((a*b) / nwd(a,b))

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))

print(f"NWD z {a} i {b} to {nwd(a,b)}, a NWW to {nww(a,b)}")
