"""
In this problem, the task is to read a code of a product 1, 
the number of units of product 1, the price for one unit of 
product 1, the code of a product 2, the number of units of 
product 2 and the price for one unit of product 2. After this, 
calculate and show the amount to be paid.

Input
The input file contains two lines of data. In each line there 
will be 3 values: two integers and a floating value with 2 digits 
after the decimal point.

Output
The output file must be a message like the following example where 
"Valor a pagar" means Value to Pay. Remember the space after ":" 
and after "R$" symbol. The value must be presented with 2 digits after 
the point."""

p1 = input().split()
c1 = int(p1[0])
n1 = int(p1[1])
v1 = float(p1[2])

p2 = input().split()
c2 = int(p2[0])
n2 = int(p2[1])
v2 = float(p2[2])

vt = n1*v1 + n2*v2
print(f'VALOR A PAGAR: R$ {vt:.2f}')

