# Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-е простое число - 13.

# Какое число является 10001-м простым числом?
import math

def dividers(x):
    rez = [] 
    for i in range(1, math.ceil(math.sqrt(x))+1):
        if x % i == 0:
            rez.append(i)
            rez.append(x//i)
    if len(rez) == 2:
        return True


count = 0
y = 1

while count < 10001:
    if dividers(y): 
        count += 1
        if count == 10001: break
    y += 1

print(y)
