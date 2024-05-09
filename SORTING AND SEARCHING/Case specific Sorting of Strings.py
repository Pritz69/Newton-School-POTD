# Your code here
u=[]
l=[]
s=input()
for x in s :
    if 65 <= ord(x) <= 90 :
        u.append(x)
    else :
        l.append(x)
u.sort()
l.sort()
ns=""
i,j=0,0
for x in s :
    if 65<=ord(x) <=90 :
        ns += u[i]
        i +=1
    else :
        ns +=l[j]
        j +=1 
print(ns)
