# Your code here
a,b=map(int,input().split())
m=min(a,b)
c=0
for i in range(1,m+1) :
    if a%i==0 and b%i==0 :
        c +=1
print(c)
