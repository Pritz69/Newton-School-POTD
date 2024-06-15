# Your code here
l=list(map(int,input().split()))
r=l[0]+l[1]+l[2] - min(l[0],l[1],l[2])
s=l[3]+l[4]+l[5]-min(l[4],l[3],l[5])
if r > s :
    print("Ram")
elif s > r :
    print("Shyam")
else :
    print("Tie")
