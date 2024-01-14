--->https://my.newtonschool.co/playground/code/lo1njoltyg53



n=int(input())
dp=[0]*(n+1)
dp[0]=1
dp[1]=1
dp[2]=2
for i in range(2,n+1):
    dp[i]=(dp[i-1]+dp[i-2]+dp[i-3])%1000000007
print(dp[n])
