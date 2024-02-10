---->https://my.newtonschool.co/playground/code/z4dlkmu2311g



# Your code here
n=int(input())
l=list(map(int,input().split()))
k=int(input())
l.sort()
p=l[0]
m=0
c=1
for i in range(1,n) :
    if abs(l[i]-p) > k :
        m=max(m,c)
        c=1
    else :
        c +=1
    p=l[i]
m=max(m,c)
print(n-m)
