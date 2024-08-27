# Your code here
for i in range(int(input())) :
    n,x,k=map(int,input().split())
    gb=x//k
    gg=(n-x)//k
    rb=x-(k*gb)
    rg=(n-x)-(k*gg)
    ans=min(rb,rg)
    fans = (rb-ans) + (rg-ans)
    print(fans)
