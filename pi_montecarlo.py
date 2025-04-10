'''
Wyznaczanie liczby PI metodą Monte Carlo 
'''
import tkinter as tk
import random as rd
import matplotlib
import matplotlib.pyplot as plt 
matplotlib.use('TkAgg')


w_kole = 0 

n = int(input("Podaj liczbę punktów: "))
fig, ax = plt.subplots()

for i in range(n):
    x = rd.uniform(-1,1) # uniform generuje float w podanym zakresie
    y = rd.uniform(-1,1)
    if ((x**2) + (y**2)) <= 1:
        w_kole += 1
        ax.scatter(x, y, alpha = 0.5, color = "red")
    else:
        ax.scatter(x, y, alpha = 0.5, color = "blue")

    
pi = float(4 * w_kole / n)
print(f"PI dla n = {n} wynosi {pi}.")
ax.grid(True)
ax.set_title(r'PI = ' + str(pi))
plt.show()



