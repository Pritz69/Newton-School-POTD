--->https://my.newtonschool.co/playground/code/1hq66inn6arm



# Your code here
n,k=map(int,input().split())
ans=0
if n%2==1 :
    if k>=(n+n) :
        ans=(n+n)-1
    else :
        ans=k
else :
    if k>=(n+n) :
        ans=(n+n)
    else :
        ans=k
print(ans)
