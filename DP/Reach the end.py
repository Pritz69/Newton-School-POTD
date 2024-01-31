--->https://my.newtonschool.co/playground/code/vvzvbsg0oeio


n = int(input())
mod = 10**9 + 7
dp=[0]*(n+1)
dp[0]=1
dp[1]=1
for i in range(2,n+1) :
    dp[i]=(dp[i-1]+dp[i-2])%mod 
print(dp[n])


import sys  
sys.setrecursionlimit(1000000) 
n = int(input())
mod = 10**9 + 7

def rec(i, dp):
    if i >= n:
        if i == n:
            return 1
        return 0
    if i in dp:
        return dp[i]
    c = 0
    c = (c + rec(i + 1, dp) + rec(i + 2, dp)) % mod
    dp[i] = c
    return c

dp = {}
print(rec(0, dp))
