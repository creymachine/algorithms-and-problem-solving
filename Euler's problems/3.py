# Простые делители числа 13195 - это 5, 7, 13 и 29.

# Каков самый большой делитель числа 600851475143, являющийся простым числом?
import math


def dividers(x):
    rez = [] 
    for i in range(1, math.ceil(math.sqrt(x))+1):
        if x % i == 0:
            rez.append(i)
            rez.append(x//i)
    return rez

maxs = 0

for i in dividers(600851475143):
    if len(dividers(i)) == 2:
        maxs = max(maxs, i)

print(maxs)