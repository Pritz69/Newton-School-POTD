# Your code here
for _ in range(int(input())) :
    n,a,b=map(int,input().split())
    if n%2==0 :
        o,e=n//2,n//2
    else :
        o,e=(n//2)+1,n//2
    print(o*b+e*a)
