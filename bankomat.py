'''
Aplikacja wydająca resztę.
'''

nominaly = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.20, 0.10]
dowyplaty = []


def bank(kw,wp):
    i=0
    r = wp - kw
    while r!=0 and i<len(nominaly):
        if r >= nominaly[i]:
            ile = int(r/nominaly[i])
            print(f"{ile}, {nominaly[i]}")
            
            r -= ile*nominaly[i]
            r = round(r,1)
            for j in range(ile):
                dowyplaty.append(nominaly[i])
        i+=1
    return dowyplaty


#=============================================================

kw = float(input("Podaj kwotę do zapłaty: "))# Do zapłaty
wp = float(input("Podaj wartość wpłaty: "))# Tyle dałem

print(bank(kw,wp))



