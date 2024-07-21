# Your code here
D,d,p,q=map(int,input().split())
c=0
i=1
m=0
while i <= D :
    m +=p
    c +=1
    if c==d :
        p +=q 
        c=0
    i +=1
print(m)
