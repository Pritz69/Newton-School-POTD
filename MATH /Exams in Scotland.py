# Your code here
for _ in range(int(input())) :
    x,y,z=map(int,input().split())
    if (z/(x*y)) > 0.5 :
        print("Yes")
    else :
        print("No")
