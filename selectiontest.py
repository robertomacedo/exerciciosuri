"""
Leia 4 valores inteiros A, B, C e D. 
Então se B for maior que C e D é maior que A

e se a soma de C e D for maior que a soma de A e B 

e se C e D foram valores positivos

e se A for mesmo, escreva a mensagem "Valores aceitos"
Caso contrário, escreva a mensagem "Valores nao aceitos"
"""
seq = input().split()

a = int(seq[0])
b = int(seq[1])
c = int(seq[2])
d = int(seq[3])


verificar = b > c

verificar = verificar and d > a 

verificar = verificar and c + d > a + b

verificar = verificar and c > 0 and d > 0

verificar = verificar and a % 2 == 0

if (verificar):
    print('Valores aceitos')
else:
    print('Valores não aceitos')





