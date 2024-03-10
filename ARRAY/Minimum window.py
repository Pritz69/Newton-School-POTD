--->https://my.newtonschool.co/playground/code/9swyr78q409o



# Your code here
from collections import defaultdict
t=int(input())
for _ in range(t) :
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    d=defaultdict(int)
    m=float('inf')
    i,j=0,0
    while j < n :
        d[l[j]]=d.get(l[j],0)+1
        while i<n and len(d) >= k :
            if len(d)==k :
                m=min(m,j-i+1)
            d[l[i]] -=1
            if d[l[i]]==0 :
                d.pop(l[i])
            i +=1
        
        j +=1
    print(m)
