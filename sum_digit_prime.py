from math import isqrt
def is_prime(n):
    if n<2:
        return False
    for i in range(2,isqrt(n)+1):
        if n%i==0:
            return False
    return True

def digit_sum_is_prime(num):
    total = sum(int(d) for d in str(num))
    return is_prime(total)


def is_valid_special_prime(num):
    return (
        is_prime(num) and
        digit_sum_is_prime(num)
    )
def find_special_3d_primes():
    print("3-digit numbers that satisfy all conditions:\n")
    for num in range(100, 1000):
        if is_valid_special_prime(num):
            print(num)