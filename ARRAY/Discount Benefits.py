# Your code here
n,x,y=map(int,input().split())
l=list(map(int,input().split()))
s=sum(l)
nc=0
for e in l :
    nc += max(0,e-y)
if s > (x+nc) :
    print("COUPON")
else :
    print("NO COUPON")
