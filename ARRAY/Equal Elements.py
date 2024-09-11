# Your code here
for _ in range(int(input())) :
    n=int(input())
    l=list(map(int,input().split()))
    d={}
    for x in l :
        d[x]=d.get(x,0)+1
    d=dict(sorted(d.items(),key=lambda x:x[1] ))
    m=0
    for x in d :
        m=max(m,d[x])
    print(n-m)
