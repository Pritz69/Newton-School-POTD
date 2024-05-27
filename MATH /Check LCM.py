# Your code here
n=int(input())
from math import gcd

def MaxLCM(n) :
 
    # if n is odd
    if (n % 2 != 0) :
        print(n*(n - 1)*(n - 2))
 
    # if n is even and n, n-3 gcd is 1
    elif (gcd(n, (n - 3)) == 1) :
        print(n*(n - 1)*(n - 3))
 
    else :
        print((n - 1)*(n - 2)*(n - 3))

MaxLCM(n)
