import math
"""
You must make a program that read a float-point number and print 
a message saying in which of following intervals the number belongs: 
[0,25] (25,50], (50,75], (75,100]. If the read number is less than zero 
or greather than 100, the program must print the message “Fora de intervalo” 
that means "Out of Interval".

The symbol '(' represents greather than. For example:
[0,25] indicates numbers between 0 and 25.0000, including both.
(25,50] indicates numbers greather than 25 (25.00001) up to 50.0000000.
"""
# valor = float(input())

# if 0<=valor<=25:
#     print('Intervalo [0, 25]')
# elif 25<valor<=50:
#     print('Intervalo (25,50]')
# elif 50<valor<=75:
#     print('Intervalo (50,75]')
# elif 75<valor<=100:
#     print('Intevalo (75,100]')
# else:
#     print('Fora de intervalo')

r = input().split()

a = float(r[0])
b = float(r[1])
c = float(r[2])

delta = (b ** 2) - (4 * a * c)

if (delta < 0):
    print('Impossivel calcular')


if (delta > 0):
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)

    print(f"R1 = {x1:.5f}")
    print(f"R2 = {x2:.5f}")
