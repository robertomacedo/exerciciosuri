"""
if A ≥ B + C, write the message: NAO FORMA TRIANGULO
if A2 = B2 + C2, write the message: TRIANGULO RETANGULO
if A2 > B2 + C2, write the message: TRIANGULO OBTUSANGULO
if A2 < B2 + C2, write the message: TRIANGULO ACUTANGULO
if the three sides are the same size, write the message: TRIANGULO EQUILATERO
if only two sides are the same and the third one is different, write the message: TRIANGULO ISOSCELES
"""

dado = input().split()

a = float(dado[0])
b = float(dado[1])
c = float(dado[2])


if a == b + c:
    print('Triangulo retangulo')

if a**2 > b**2 + c**2:
    print('Triangulo obtusangulo')

if a == b == c == a:
    print('Triagulo isosceles')

if a**2 < b**2 + c**2:
    print('Triangulo acutangulo')

if a <= b+c: 
    print('Não forma triangulo')

else:
    pass
