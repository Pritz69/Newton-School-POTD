---->https://my.newtonschool.co/playground/code/skc1egkkzmlk



# Your code here
n=int(input())
l=list(map(int,input().split()))
d={}
for x in l :
    d[x]=d.get(x,0)+1
for x in d :
    if d[x]==1 :
        print(x)
        exit()
print(-1)
