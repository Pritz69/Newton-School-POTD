# Your code here
n=int(input())
l=list(map(int,input().split()))
mi,ma=min(l),max(l)
ans=float('inf')
for i in range(mi,ma+1) :
    s=0
    for x in l :
        s += (x-i)**2
    ans=min(ans,s)
print(ans)
