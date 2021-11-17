"""
if A ≥ B + C, write the message: NAO FORMA TRIANGULO
if A2 = B2 + C2, write the message: TRIANGULO RETANGULO
if A2 > B2 + C2, write the message: TRIANGULO OBTUSANGULO
if A2 < B2 + C2, write the message: TRIANGULO ACUTANGULO
if the three sides are the same size, write the message: TRIANGULO EQUILATERO
if only two sides are the same and the third one is different, write the message: TRIANGULO ISOSCELES
"""

a, b, c = sorted(list((map(float, input().split()))), reverse=True)


if a >= (b + c):
    print('NAO FORMA TRIANGULO')
elif a**2 == (b**2+c**2):
    print('TRIANGULO RETANGULO')
elif a**2 > (b**2+c**2):
    print('TRIANGULO OBTUSANGULO')
elif a**2 < (b**2+c**2):
    print('TRIANGULO ACUTANGULO')

if a == b == c:
    print('TRIANGULO EQUILATERO')

elif a == b or b == c:
    print('TRIANGULO ISOSCELES')
