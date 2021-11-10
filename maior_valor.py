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
