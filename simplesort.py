"""
Read three integers and sort them in ascending order. 
After, print these values in ascending order, a blank 
line and then the values in the sequence as they were readed.
"""

valors = list(map(int, input().split()))


for valor in sorted(valors):
    print(valor)

print()

for valor in valors:
    print(valor)
