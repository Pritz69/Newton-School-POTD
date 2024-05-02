# Your code here
a=[]
dp=['NULL' for x in range(100001)]
def f(n):
    n=int(n)
    if dp[n]!='NULL':
        return dp[n]
    res='No'
    if n==1:
        res='Yes'
    for x in a:
        if n%x==0:
            res=f(n/x)
    dp[n]=res
    return res
for i in range(100001):
    s=str(i)
    ok=1
    for j in s:
        if j!='1' and j!='0':
            ok=0
    if ok==1 and i!=0 and i!=1:
        a.append(i)

n=int(input())
print(f(n))
