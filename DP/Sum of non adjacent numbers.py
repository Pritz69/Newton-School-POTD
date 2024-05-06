# Your code here
n=int(input())
l=list(map(int,input().split()))
def rec(i) :
    if i>=n :
        return 0
    if i in dp :
        return dp[i]
    tk=0
    ntk=0
    tk=tk+l[i]+rec(i+2)
    ntk=ntk+rec(i+1)
    dp[i]=max(tk,ntk)
    return dp[i]
dp={}
print(rec(0))
