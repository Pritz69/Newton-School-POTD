# Your code here
n=int(input())
l=list(map(int,input().split()))
s=sum(l)
if s==0:
    print(2)
elif s%2==0 :
    print(0)
else :
    print(1)
