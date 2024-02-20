# Your code here
n=int(input())
l=list(map(int,input().split()))
k=int(input())
d={}
for x in l :
    d[x]=d.get(x,0)+1
d=dict(sorted(d.items(),key=lambda x:(x[1],x[0]),reverse=True))
ans=""
for x in d :
    if k==0:
        break
    ans =ans + str(x) + " "
    k -=1
print(ans)
