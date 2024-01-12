---->https://my.newtonschool.co/playground/code/3yv9ht0cuoio



# Your code here
n,k=map(int,input().split())
l=list(map(int,input().split()))
c=0
ma=0
for i in range(n) :
    ma=max(ma,l[i])
    mi=float('inf')
    for j in range(i+1,n) :
        mi=min(mi,l[j])
    if mi != float('inf'):
        if ma+mi >= k :
            c +=1
print(c)
