--->https://my.newtonschool.co/playground/code/vvzvbsg0oeio



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
