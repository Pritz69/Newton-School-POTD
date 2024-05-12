# Your code here
n=int(input())
l=list(map(int,input().split()))
m=float('-inf')
cmsm=sum(l)
v=0
for i in range(n) :
    v += i*l[i]
m=max(m,v)
for i in range(1,n) :
    nv= v - (cmsm-l[i-1]) + (l[i-1]*(n-1))
    v=nv
    m=max(m,nv)
print(m)
