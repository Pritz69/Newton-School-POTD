# Your code here
n=int(input())
l=list(map(int,input().split()))
s=sum(l)
ans=float('inf')
c=0
m=float('inf')
for x in l :
    c +=x 
    d=abs(c-(s-c)) 
    if d < m :
        m=d
        ans=min(ans,max(c,s-c))
print(ans)
