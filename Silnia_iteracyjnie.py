n = int(input("podaj liczbę n: "))
if n<2:
    print(f"Silnia z {n} wynosi 1")
else :
    for i in range(1, n+1):
        n *= i
    print(f"Silnia z {n} wynosi 1")