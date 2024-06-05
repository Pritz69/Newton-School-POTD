# Your code here
n=int(input())
l=list(map(int,input().split()))
x=0
for e in l :
    x=x^e 
ans=x
for e in l :
    ans=min(ans,x^e)
print(ans)
