--->https://my.newtonschool.co/playground/code/tvczkbdqgwbp



# Your code here
n=int(input())
c=list(map(int,input().split()))
l={}
for x in c :
    l[x]=l.get(x,0)+1
lt=0
f=0
if 0 in l :
    lt=0
    l[0]-=1
else :
    f=1
l=dict(sorted(l.items(),key=lambda x:x[0],reverse=True))
num=0
for x in l :
    for c in range(l[x]):
        num = num*10 + int(x)
num=num*10 + lt
print(num if f==0 else  -1)
