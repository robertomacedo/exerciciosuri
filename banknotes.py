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

"""
Read an integer value corresponding to a person's age (in days) 
and print it in years, months and days, followed by its respective 
message “ano(s)”, “mes(es)”, “dia(s)”.

Note: only to facilitate the calculation, consider the whole year 
with 365 days and 30 days every month. In the cases of test there 
will never be a situation that allows 12 months and some days, like 
360, 363 or 364. This is just an exercise for the purpose of testing 
simple mathematical reasoning.

Input
The input file contains 1 integer value.

Output
Print the output, like the following example
"""


dias = int(input())


ano = dias // 365
meses = dias % 365//30
dias = dias % 365
dias = dias % 30

print(f'{ano} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')