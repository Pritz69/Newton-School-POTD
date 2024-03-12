---->https://my.newtonschool.co/playground/code/ufa3nl9uskmh



# Your code here
m,n=map(int,input().split())
l=list(map(int,input().split()))
s=sum(l) 
if s > m :
    print(-1)
else :
    print(m-s)
