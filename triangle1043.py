'''Calcular area e peimetro de um triangulo uri1043'''

a, b, c = sorted(list((map(float, input().split()))), reverse=True)

if a + b > c and a + c > b and b + c > a:
    print(f'Perimetro = {(a + b + c):.1f}')

else:
    print(f'Area = {(0.50 * (a + b) * c):.1f}')
