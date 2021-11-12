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

"""
Two cars (X and Y) leave in the same direction. The car X leaves with 
a constant speed of 60 km/h and the car Y leaves with a constant speed of 90 km / h.

In one hour (60 minutes) the car Y can get a distance of 30 kilometers 
from the X car, in other words, it can get away one kilometer for each 2 minutes.

Read the distance (in km) and calculate how long it takes (in minutes) 
for the car Y to take this distance in relation to the other car.

Input
The input file contains 1 integer value.

Output
Print the necessary time followed by the message "minutos" that means minutes in Portuguese
"""


x = int(input())  # entrada em km

resp = x * 2  

print(f'{resp} minutos')
