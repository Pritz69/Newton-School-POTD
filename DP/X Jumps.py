# Your code here
for i in range(int(input())) :
    x,y=map(int,input().split())
    def rec(n) :
        if n==x :
            return 0
        if n > x :
            return float('inf')
        if n in dp :
            return dp[n]
        ans=0
        ans = ans+ 1 + min(rec(n+y),rec(n+1))
        dp[n]=ans
        return ans 
    dp={}
    print(rec(0))
