# Your code here
n,x=map(int,input().split())
c=0
i=0
while i <= n-(3*x) :
    i +=(3*x)
    c +=1
print(c) 
