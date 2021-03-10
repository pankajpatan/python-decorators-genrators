from math import sqrt
# #second question
print('Prime Numbers With Genrators ')
def is_prime(n):
    if n<=1:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    i =3
    while i<= sqrt(n):
        if n%i==0:
            return False
        i=i+2
    return True

def prime_genrator():
    n=1
    while True:
        n += 1
        if is_prime(n):
            yield n


genrator = prime_genrator()

for i in range(10):
    print(next(genrator))