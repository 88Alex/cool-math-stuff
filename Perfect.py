import time
def sumOfFactors(a):
    factors=[]
    i=1
    while i<a:
        if(a%i==0):
            factors.append(i)
    i=i+1
    sum=0
    for q in factors:
        sum = sum + q
    return sum
number = int(raw_input("Maximum number to check? "))
i=2
while i<=number:
    factorSum = sumOfFactors(i)
    if factorSum < i:
        print(i," is deficient.")
    elif factorSum > i:
        print(i," is abundant!")
    elif factorSum == i:
        print(i," is PERFECT!!!")
    time.sleep(0.5)
