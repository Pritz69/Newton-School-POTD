# Your code here
for _ in range(int(input())) :
    a,b=map(int,input().split())
    f=100-a
    s=200-(2*b)
    if f<s :
        print("First")
    elif s < f :
        print("Second")
    else :
        print("Both")
