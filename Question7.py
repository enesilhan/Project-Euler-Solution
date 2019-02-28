
from math import sqrt

def prime(num):
    i = 2
    while i <= sqrt(num):
        if num%i == 0 and num != i:
            return False
        i += 1
    return True


n = 0
i = 1
while n < 10001:
    i += 1
    if prime(i):
        n += 1

print("10001. Prime Number :",i)