# Your code here
n=int(input())
li=list(map(int,input().split()))
ans=0
l=0
for i in range(n) :
    if li[i]==0 :
        l=i 
    else :
        ans=max(ans,(i-l))
print(ans) 
