# Your code here
for _ in range(int(input())) :
    n=int(input())
    l=list(map(int,input().split()))
    o,e=0,0
    for x in l :
        if x%2==0 :
            e +=1
        else :
            o +=1
    if o%2==0 :
        print("Yes")
    else :
        print("No")
