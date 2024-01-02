--->https://my.newtonschool.co/playground/code/zf154gez2b8k



# Your code here
import math
n=int(input())
l=list(map(int,input().split()))
s=sum(l)
def isprime(x) :
    for i in range(2,int(math.sqrt(x))+1) :
        if x%i==0 :
            return False
    return True
i=s 
while not isprime(i) :
    i +=1
print(i-s)
