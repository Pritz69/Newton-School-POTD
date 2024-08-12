# Your code here
for _ in range(int(input())) :
    x,y=map(int,input().split())
    for i in range(y) :
        x=max(x+1000,x+x)
    print(x)
