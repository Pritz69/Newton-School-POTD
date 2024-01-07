-->https://my.newtonschool.co/playground/code/m8x9xbq9nwoz



# Your code here
import math
n=int(input())
s=list(map(int,input().split()))
l=set([i*i for i in s])
f=0
for i in range(n) :
    for j in range(i+1,n) :
        if (s[i]*s[i] + s[j]*s[j]) in l :
            f=1
            break
print("Yes") if f==1 else print("No")
