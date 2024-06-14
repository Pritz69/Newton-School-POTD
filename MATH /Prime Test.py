# Your code here
def isprime(x) :
    if x==2 or x==3 :
        return True
    for i in range(2,int(x**0.5)+1) :
        if x%i==0 :
            return False
    return True
n=int(input())
if isprime(n) :
    print("Yes")
else :
    print("No")
