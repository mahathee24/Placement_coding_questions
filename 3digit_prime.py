#Print 20 number of 3 digit prime numbers that possibly least numbers
a=100
count=0
while count < 20:
    is_prime=True
    for i in range(2,int(a**0.5     )+1):
        if a %i == 0:
            is_prime=False
            break
    if is_prime:
        print(a)
        count += 1
    a += 1
        
