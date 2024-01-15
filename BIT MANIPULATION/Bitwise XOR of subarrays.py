--->https://my.newtonschool.co/playground/code/94l0vpoy7ynv



# Your code here
n=int(input())
l=list(map(int,input().split()))
x=0
for i in range(n) :
    v=l[i]
    cnt=(i+1)*(n-i)
    if cnt%2==1 :
        x=x^v
print(x)
