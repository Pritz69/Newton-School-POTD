---->https://my.newtonschool.co/playground/code/4w387alerc3q



# Your code here
n,m,z=map(int,input().split())
c,d=n,m
ans=0
s=set()
while c<=z :
    s.add(c)
    c +=n 
while d<=z :
    if d in s :
        ans +=1
    d +=m
print(ans)
