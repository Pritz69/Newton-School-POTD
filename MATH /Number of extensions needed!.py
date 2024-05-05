# Your code here
a,b=map(int,input().split())
c=1
s=a
if b==1 :
    print(0)
elif (b<=a) :
    print(1)
else :
    while s < b :
        c +=1
        s +=(a-1)
    print(c)
