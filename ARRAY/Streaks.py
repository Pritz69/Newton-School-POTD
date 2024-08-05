# Your code here
for _ in range(int(input())) :
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=0
    ma=0
    for i in range(n) :
        if a[i]==0 or b[i]==0 :
            ma=max(ma,c)
            c=0
        else :
            c +=1
    ma=max(ma,c)
    print(ma)
