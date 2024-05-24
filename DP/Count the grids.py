# Your code here
n=int(input())
dp=[0]*(n+1)
for i in range(1,4) :
    dp[i]=1
dp[4]=2
for i in range(5,n+1) :
    dp[i]=dp[i-1]+dp[i-4]
print(dp[n])
