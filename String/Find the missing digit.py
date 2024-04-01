# Your code here
s=input()
d={}
for x in s :
    d[x]=d.get(x,0)+1
for i in range(10) :
    if str(i) not in d :
        print(i)
