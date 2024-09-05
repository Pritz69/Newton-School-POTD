# Your code here
for _ in range(int(input())) :
    x,y=map(int,input().split())
    if (y%x)==0 :
        print("YES")
    elif y >= (2*x):
        print("YES")
    else :
        print("NO")
