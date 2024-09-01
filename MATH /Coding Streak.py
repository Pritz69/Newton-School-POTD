# Your code here
for i in range(int(input())) :
    n=int(input())
    l=list(map(int,input().split()))
    l1=list(map(int,input().split()))
    o,a=0,0
    c=0
    for x in l :
        if x==0 :
            o=max(o,c)
            c=0
        else :
            c +=1
    o=max(o,c)
    c=0
    for x in l1 :
        if x==0 :
            a=max(a,c)
            c=0
        else :
            c +=1
    a=max(a,c)
    if o > a :
        print("Orry")
    elif a >o :
        print("Adi")
    else :
        print("Dabur")
