# Your code here
for _ in range(int(input())) :
    a,b,c=map(int,input().split())
    if a==(b+c) :
        print("Yes")
    elif b==(a+c) :
        print("Yes")
    elif c==(a+b) :
        print("Yes")
    else :
        print("No")
