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

A = float(5.0)
B = float(7.1)

MEDIA = ((A*3.5) + (B*7.5))/(3.5 + 7.5)

print(f'MEDIA = {MEDIA:.5f}')
