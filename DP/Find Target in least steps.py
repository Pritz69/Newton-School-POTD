def tabulate_rec(t):
    dp = [float('inf')] * (t + 1)
    dp[0] = 0
    
    for i in range(1, t + 1):
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i - 1] + 1, dp[i // 2] + 1)
        else:
            dp[i] = min(dp[i], dp[i - 1] + 1)
    
    return dp[t]

t = int(input())
print(tabulate_rec(t))



t=int(input())
def rec(i) :
    if i==0:
        return 0
    if i<0 :
        return float('inf')
    if i in dp :
        return dp[i]
    if i%2==0 :
        c=1+min(rec(i-1),rec(i//2))
    else :
        c=1+rec(i-1)
    dp[i]=c
    return c
dp={}
print(rec(t))
