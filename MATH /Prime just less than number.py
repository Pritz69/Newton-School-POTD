---->https://my.newtonschool.co/playground/code/3r18cbnufgvw



# Your code here
from math import sqrt
def isprime(x) :
    if x<=1 :
        return 0
    if x==2 or x==3 :
        return 1
    for i in range(2,int(sqrt(x))+1) :
        if x%i==0 :
            return 0
    return 1
n=int(input())
while not isprime(n) :
    n -=1
print(n)
