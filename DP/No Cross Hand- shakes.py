# Your code here
---->https://my.newtonschool.co/playground/code/bpvto8lt7nfv

N=int(input())
dp=[0]*(N+1)
dp[0]=1
for i in range(2,N+1,2) :
    for j in range(0,(N-2)+1,2) :
        dp[i] = dp[i] + dp[j]*dp[i-2-j]
print(dp[N])
