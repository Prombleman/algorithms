'''
NWD:
- metoda reszt  dzielenia
- metoda Euklidesa
'''
a = int(input("Podaj a: "))
b = int(input("Podaj b: "))

# def nwd(a,b):
#     r = -1
#     while r!=0 :
#         r = a % b
#         a = b
#         b = r
#     return a 

def nwd_euklides(a,b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


print(f"NWD dla {a} oraz {b} to {nwd_euklides(a,b)}")

