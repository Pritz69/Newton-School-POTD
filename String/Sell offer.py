# Your code here
s=input()
d={}
for x in s :
    d[x]=d.get(x,0)+1
c=0
for x in d :
    if d[x]%2==0 :
        c += d[x]//2
    else :
        c += d[x]//2 + 1
print(c)
