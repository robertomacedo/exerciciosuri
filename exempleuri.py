"""
Solução uri exemples

Read 2 variables, named A and B and make the sum of these two variables, assigning its result to the variable X. Print X as shown below. Print endline after the result otherwise you will get “Presentation Error”.

Input
The input file will contain 2 integer numbers.

Output
Print the letter X (uppercase) with a blank space before and after the equal signal followed by the value of X, according to the following example.

Obs.: don't forget the endline after all

"""

A = 10
B = 9

X = A + B

print('X = ', X) 


"""
Read two floating points' values of double precision A and B, corresponding 
to two student's grades. After this, calculate the student's average, considering 
that grade A has weight 3.5 and B has weight 7.5. Each grade can be from zero to ten, 
always with one digit after the decimal point. Don’t forget to print the end of line 
after the result, otherwise you will receive “Presentation Error”. Don’t forget the space 
before and after the equal sign.

Input
The input file contains 2 floating points' values with one digit after the decimal point.

Output
Print the message "MEDIA"(average in Portuguese) and the student's average according to 
the following example, with 5 digits after the decimal point and with a blank space before 
and after the equal signal"""

A = float(input())
B = float(input())

MEDIA = (A*3.5 + B*7.5)/(3.5 + 7.5)

print(f'MEDIA = {MEDIA:.5f}')


"""
Read three values (variables A, B and C), which are the three student's grades. Then, 
calculate the average, considering that grade A has weight 2, grade B has weight 3 and 
the grade C has weight 5. Consider that each grade can go from 0 to 10.0, always with one 
decimal place.

Input
The input file contains 3 values of floating points (double) with one digit after 
the decimal point.

Output
Print the message "MEDIA"(average in Portuguese) and the student's average according to 
the following example, with a blank space before and after the equal signal.
"""

A = float(input())
B = float(input())
C = float(input())

MEDIA = (A*2 + B*3 + C*5)/(2 + 3 + 5)

print('MEDIA = ', MEDIA)
print(f'MEDIA = {MEDIA:.1f}')



"""
Welcome to beecrowd!

Your first program in any programming language is usually "Hello World!". In this first problem 
all you have to do is print this message on the screen.

Input
This problem has no input.

Output
You must print the message Hello World! and then the endline as shown below"""

r = float(input())
a = 3.14159 * (r**2)

print(f'A={a:.4f}')



n = int(input())
h = float(input())
s = float(input())

r = h*s

print(f'NUMBER = {n}')
print(f'SALARY = U$ {r:.2f}')

"""
Make a program that reads a seller's name, his/her fixed salary and 
the sale's total made by himself/herself in the month (in money). 
Considering that this seller receives 15% over all products sold, 
write the final salary (total) of this seller at the end of the month, 
with two decimal places."""

name = str(input())
s_fixo = float(input())
vendas = float(input())

perc = vendas * 0.15
total = s_fixo + perc

print(name)
print(f'TOTAL = U$ {total:.2f}')
