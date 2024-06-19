# Your code here
n,b,m=map(int,input().split())
ans=0
while n :
    if n%2==0 :
        p=n//2
        n=n-p
    else :
        p=(n+1)//2
        n=n-p
    ans += p*m 
    if n!=0 :
        ans +=b
    m*=2
print(ans)
