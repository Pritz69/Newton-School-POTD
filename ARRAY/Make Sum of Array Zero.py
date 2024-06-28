# Your code here
n=int(input())
l=list(map(int,input().split()))
c0,c1=0,0
for x in l :
    if x==-1 :
        c0 +=1
    else :
        c1 +=1
if c1==c0 :
    print(0)
else :
    if (c0-c1)%2==0 :
        print(abs(c0-c1)//2)
    else :
        print(-1)
