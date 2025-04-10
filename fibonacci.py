'''
Ciąg Fibonacciego
'''

n = int(input("Podaj n: "))

def fib(n):
    if n < 2:
        return n 
    return fib(n-1)+fib(n-2)

print(fib(n))
lista = [fib(i) for i in range(n+1)]
print(f"Ciąg Fibonacciego: {lista}")
print(f"Suma elementów ciągu: {sum(lista)}")