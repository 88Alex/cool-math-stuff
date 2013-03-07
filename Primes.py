import time
def isPrime(a):
    i=2
    while i<a:
        if a%i==0:
            return False
        i=i+1
    return True
number=int(input("Maximum number to check? "))
q=2
while q<=number:
    if isPrime(q):
        print(q," is PRIME!!!")
    else:
        print(q," is not prime.")
    time.sleep(0.5)
    q=q+1
