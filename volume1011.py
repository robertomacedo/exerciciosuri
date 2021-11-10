"""
Make a program that calculates and shows the volume of a sphere being 
provided the value of its radius (R) . The formula to calculate the volume is: 
(4/3) * pi * R3. Consider (assign) for pi the value 3.14159.

Tip: Use (4/3.0) or (4.0/3) in your formula, because some languages (including 
C++) assume that the division's result between two integers is another integer. :)

Input
The input contains a value of floating point (double precision).

Output
The output must be a message "VOLUME" like the following example with a space 
before and after the equal signal. The value must be presented with 3 digits 
after the decimal point.

"""

raio = int(input())
pi = 3.14159

result = (4.0/3) * pi * (raio ** 3)

print(f'VOLUME = {result:.3f}')


"""
Make a program that reads three floating point values: A, B and C. Then, calculate and show:
a) the area of the rectangled triangle that has base A and height C.
b) the area of the radius's circle C. (pi = 3.14159)
c) the area of the trapezium which has A and B by base, and C by height.
d) the area of ​​the square that has side B.
e) the area of the rectangle that has sides A and B.

Input
The input file contains three double values with one digit after the decimal point.

Output
The output file must contain 5 lines of data. Each line corresponds to one of the 
areas described above, always with a corresponding message (in Portuguese) and one 
space between the two points and the value. The value calculated must be presented 
with 3 digits after the decimal point
"""

dado = input().split()
a = float(dado[0])
b = float(dado[1])
c = float(dado[2]) 

tri = a*c/2
cir = 3.14159 * (c ** 2)
tra = (a+b)*c/2
squ = b*b
ret = a*b

print(f'TRIANGULO: {tri:.3f}')
print(f'CIRCULO: {cir:.3f}')
print(f'TRAPEZIO: {tra:.3f}')
print(f'QUADRADO: {squ:.3f}')
print(f'RETANGULO: {ret:.3f}')
