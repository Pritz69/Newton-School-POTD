# Your code here
n=int(input())
l=input()
d={}
f=0
for x in l :
    d[x]=d.get(x,0)+1
    if d[x]==2 :
        f=1
if f==1 :
    print(n-2)
else :
    print(-1)
