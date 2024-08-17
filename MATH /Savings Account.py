# Your code here
for _ in  range(int(input())) :
    x,y,z=map(int,input().split())
    ans=0
    s=x*y 
    while s > z :
        ans +=1
        s -=y
    print(ans)
