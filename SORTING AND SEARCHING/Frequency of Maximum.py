# Your code here
n=int(input())
l=list(map(int,input().split()))
d={}
for x in l :
    d[x]=d.get(x,0) +1
d=sorted(d.items(),key=lambda x: (-x[1],x[0]) )
print(d[0][0],d[0][1])
