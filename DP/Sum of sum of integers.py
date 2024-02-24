---->https://my.newtonschool.co/playground/code/n1fxwfxnrba0



# Your code here
dp=[0]*(100001)
def sm(x) :
    s=0
    while x :
        s += x%10
        x = x//10
    return s 
for i in range(1,100001) :
    dp[i]=sm(i)
ans=0
n=int(input())
for i in range(n+1)  :
    ans += dp[i]
print(ans)
