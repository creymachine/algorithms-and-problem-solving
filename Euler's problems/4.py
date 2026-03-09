# Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. Самое большое число-палиндром, 
# полученное умножением двух двузначных чисел – 9009 = 91 × 99.

# Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.

def palindrom(x):
    x = str(x)
    if len(x) % 2 == 0:
        s1 = x[0:(len(x)//2)]
        s2 = x[-1:(len(x)//2)-1:-1]
        if s1 == s2: return True
        else: return False

    elif len(x) == 1: return True

    elif len(x) % 2 != 0:
        s = x[0]
        for i in x:
            if i != s: return False
        return True

m = 0

for x in range(100,1000):
    for y in range(100,1000):
        if palindrom(x*y):
            m = max(m, x*y)

print(m)
