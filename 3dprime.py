def prime(i):
    if i <= 1:
        return False
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            return False
    return True

def sod(i):
    d = list(str(i))
    x = sum([int(j) for j in d])
    return prime(x)

def dig(i):
    while i > 0:
        d = i % 10
        if not prime(d):  
            return False
        i = i // 10
    return True

for i in range(100, 1000):
    if prime(i) and sod(i) and dig(i):
        print(i, end=" ")
