# Your code here
n=int(input())
mod=10**9 + 7
ans=((n+1)*(n+2))%mod
ans =(ans//2)%mod
print(ans)
