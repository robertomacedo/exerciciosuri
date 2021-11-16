"""
Using the following table, write a program that reads a code 
and the amount of an item. After, print the value to pay. This 
is a very simple program with the only intention of practice of 
selection commands
"""

pedido = input().split()

cod = int(pedido[0])
qtd = int(pedido[1])
total = 0.0

if cod == 1:
    total = 4.0 * qtd
elif cod == 2:
    total = 4.5 * qtd
elif cod == 3:
    total = 5.0 * qtd
elif cod == 4:
    total = 2.0 * qtd
elif cod == 5:
    total = 1.5 * qtd

print(f'Total: R$ {total:.2f}')

