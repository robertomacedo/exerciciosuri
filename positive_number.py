"""
Leia seis valores e conte quais desses são positivos e imprima
exemplo (4 valores positivos)
"""


# num = input().split()

lista = [7, -5, 6, -3.4, 4.6, 12]
p = 0.0

for n in lista:
    if n >= 0:
        p += 1

print(f'{p} valores positivos')
