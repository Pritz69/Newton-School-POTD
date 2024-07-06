c=int(input())
a,b=[],[]
c=bin(c)[2:]
f=0
for x in c :
    if x=='1' :
        if f==0 :
            f=1 
            a.append(1)
            b.append(0)
        else :
            b.append(1)
            a.append(0)
    else :
        a.append(1)
        b.append(1)
an=0
p=1 
for i in range(len(a)-1,-1,-1) :
    an = an + p*a[i] 
    p=p*2 
bn=0
p=1 
for i in range(len(b)-1,-1,-1) :
    bn = bn + p*b[i] 
    p=p*2 
    #print(a,b)
print(an*bn)
