# Your code here
for _ in range(int(input())) :
    n,x=map(int,input().split())
    l=input()
    c=0
    f=0
    for e in l :
        if e=='0' :
            c -=1
            if c <0 :
                f=1
                break
        else :
            c=x 
    if f==1 :
        print("No")
    else :
        print("Yes")
