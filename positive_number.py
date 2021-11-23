"""
Leia seis valores e conte quais desses são positivos e imprima
exemplo (4 valores positivos)
"""
# import collections
# numeros = input()

num = input().split()

lista = list(num)

p = 0.0

for n in lista:
    if n >= 0:
        p += 1

print(f'{p} valores')
