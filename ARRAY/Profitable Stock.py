# Your code here
n=int(input())
l=list(map(int,input().split()))
p=0
m=l[0]
for i in range(1,n) :
    p=max(p,l[i]-m)
    m=min(m,l[i])
print(p)
