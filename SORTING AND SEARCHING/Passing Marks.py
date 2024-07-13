# Your code here
n,x=map(int,input().split())
l=list(map(int,input().split()))
mi=min(l)
ma=max(l)
le=mi-1
ri=ma-1
ans=0
def func(t) :
    c=0
    for el in l :
        if el > t :
            c +=1
    return c 
while le<=ri :
    mi=(le+ri)//2
    if func(mi) >= x :
        ans=mi 
        le=mi+1
    else :
        ri=mi-1
print(ans)
