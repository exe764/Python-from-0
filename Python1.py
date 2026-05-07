from math import factorial

x = float(input())
n = int(input())

suma = 0.0
for i in range(n) :
    termino = (x ** i) / factorial(i)
    suma = suma + termino
print("x =", x)
print("n =", n)
print("sumatoria de serie =", suma)