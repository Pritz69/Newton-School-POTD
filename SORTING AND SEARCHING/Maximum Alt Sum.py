# Your code here
import math
for i in range(int(input())) :
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    le=math.floor(n/2)
    s1=sum(l[0:le])
    s2=sum(l[le:n])
    print(s2-s1)
