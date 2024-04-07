# Your code here
n=int(input())
if n==1 :
    print(0)
    exit()
elif n==2 :
    print(1) 
    exit()
else :
    a=0
    b=1
    s=1
    for i in range(n-2) :
        c=a+b
        s+=c
        a=b
        b=c 
    print(s)
