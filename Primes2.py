import time
def isPrime(a):
    i=2
    while i<a:
        if a%i==0:
            return False
        i=i+1
    return True
number=int(input("Minimum number to check? "))
amount=int(input("Amount of primes? "))
primesFound=0
while primesFound<amount:
    if isPrime(q):
        print(q)
        primesFound=primesFound+1
    time.sleep(0.5)
