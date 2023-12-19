---->https://my.newtonschool.co/playground/code/hn48lyyrb8f0



l,k=map(int,input().split())
pd,nd=0,0
if k==l :
    print(0)
elif k<l :
    pd=l-k
    if pd%2==0 :
        print(1)
    else :
        print(2)
else :
    nd=k-l
    if nd%2==0 :
        print(2)
    else :
        print(1)
