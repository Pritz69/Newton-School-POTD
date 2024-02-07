--->https://my.newtonschool.co/playground/code/rygfx05i40bj



# Your code here
n,c=map(int,input().split())
l=list(map(int,input().split()))
f=0
l.sort()
s=0
for i in range(n-1) :
    s +=l[i]
if s <= c :
    print("Yes")
else :
    print("No")
