import math
"""Make a program that reads 3 integer values and present 
the greatest one followed by the message "eh o maior". 
Use the following formula:


Input
The input file contains 3 integer values.

Output
Print the greatest of these three values followed 
by a space and the message “eh o maior”
"""

maior_valor = input().split()

a = int(maior_valor[0]) 
b = int(maior_valor[1])
c = int(maior_valor[2])

m = max(a, b, c)

print(f'{m} eh o maior')


"""
Calculate a car's average consumption being provided the total 
distance traveled (in Km) and the spent fuel total (in liters).

Input
The input file contains two values: one integer value X representing 
the total distance (in Km) and the second one is a floating point number 
Y  representing the spent fuel total, with a digit after the decimal point.
"""
x = int(input())
y = float(input())

result = x/y

print(f'{result:.3f} km/l')

"""
Read the four values corresponding to the x and y axes of 
two points in the plane, p1 (x1, y1) and p2 (x2, y2) and 
calculate the distance between them, showing four decimal 
places after the comma, according to the formula:

Distance = 

Input
The input file contains two lines of data. The first one 
contains two double values: x1 y1 and the second one also 
contains two double values with one digit after the decimal 
point: x2 y2.

Output
Calculate and print the distance value using the provided formula, 
with 4 digits after the decimal point.
"""
sqx = input().split()
x1 = float(sqx[0])
x2 = float(sqx[1])

sqx2 = input().split()
y1 = float(sqx2[0])
y2 = float(sqx2[1])

abc = ((x2-y1)**2 + (y2-x1))**2
sqr_x = math.sqrt(abc)

print(f'{sqr_x:.4f}')