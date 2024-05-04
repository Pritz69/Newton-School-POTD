# Your code here
n=int(input())
dp=[0]*(n+1)
dp[0]=1
dp[1]=1
dp[2]=2
dp[3]=4
for i in range(4,n+1) :
    dp[i]=(dp[i-1]+dp[i-2]+dp[i-3])%1000000007
print(dp[n])
