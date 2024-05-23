# Your code here
n=int(input())
l=list(map(int,input().split()))
def rec(N,A):
        mod = (10**9+7)
        ans = 1
        for i in range(N):
            if (A[i] & (A[i]-1)) == 0 and A[i]!=0:
                ans = (ans << 1) % mod
        return (ans-1+mod)%mod 
print(rec(n,l))
