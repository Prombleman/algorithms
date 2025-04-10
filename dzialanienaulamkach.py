'''
Działanie na ułamkach
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

l1 = int(input("Podaj licznik 1: "))
m1 = int(input("Podaj mianownik 1: "))
l2 = int(input("Podaj licznik 2: "))
m2 = int(input("Podaj minownik 2: "))
nw = nww(m1,m2)

nl1 = int((nw / m1) * l1) + int((nw / m2) * l2)
#nm1 = int(nw)
nl2 = int((nw / m1) * l1) - int((nw / m2) * l2)


if l1-l2 == 0:
    print(f"{l1}/{m1} - {l2}/{m2} = 0")
    print(f"{l1}/{m1} + {l2}/{m2} = {nl1}/{int(nw)}")
elif l1+l2 == 0:
    print(f"{l1}/{m1} + {l2}/{m2} = 0")
    print(f"{l1}/{m1} - {l2}/{m2} = {nl2}/{int(nw)}")
else:
    print(f"{l1}/{m1} + {l2}/{m2} = {nl1}/{int(nw)}")
    print(f"{l1}/{m1} - {l2}/{m2} = {nl2}/{int(nw)}")
    
    
print(f"{l1}/{m1} * {l2}/{m2} = {l1 * l2}/{m1 * m2}")
print(f"{l1}/{m1} / {l2}/{m2} = {l1 * m2}/{m1 * l2}")
