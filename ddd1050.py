"""
Read an integer number that is the code number for phone dialing. 
Then, print the destination according to the following table
"""


dict = {61: 'Brasilia',
        11: 'São Paulo',
        71: 'Salvador',
        32: 'Juiz de Fora',
        27: 'Vitoria',
        31: 'Belo Horizonte',
        21: 'Rio de Janeiro',
        19: 'Campinas',
        }

n = int(input())

print(dict[n])
