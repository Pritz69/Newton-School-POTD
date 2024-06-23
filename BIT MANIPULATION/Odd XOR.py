# Your code here
d={}
n=int(input())
l=list(map(int,input().split()))
for x in l :
    d[x]=d.get(x,0) +1
x=0
for e in d :
    if d[e] %2==1 :
        x=x^e
print(x)
