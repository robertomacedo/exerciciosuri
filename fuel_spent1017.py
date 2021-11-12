"""
Little John wants to calculate and show the amount of 
spent fuel liters on a trip, using a car that does 
12 Km/L. For this, he would like you to help him through 
a simple program. To perform the calculation, you have 
to read spent time (in hours) and the same average speed 
(km/h). In this way, you can get distance and then, 
calculate how many liters would be needed. Show the value 
with three decimal places after the poin
"""

h = int(input())  # horas 
g = int(input())  # km/h tempo gastos
consumo = 12  # litros por km/h

result = (h*g)/consumo

print(f'{result:.3f}')
