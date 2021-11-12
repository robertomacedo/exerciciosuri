"""
In this problem you have to read an integer value and 
calculate the smallest possible number of banknotes in 
which the value may be decomposed. The possible banknotes 
are 100, 50, 20, 10, 5, 2 e 1. Print the read value and the 
list of banknotes
"""

# notas = [100, 50, 20, 10, 5, 2, 1]

# entrada = int(input())

"""
Read an integer value, which is the duration 
in seconds of a certain event in a factory, 
and inform it expressed in hours:minutes:seconds
"""

segundo = int(input())

minuto = segundo // 60
segundo = segundo % 60
hora = minuto // 60
minuto = minuto % 60

print(f'{hora}:{minuto}:{segundo}')

