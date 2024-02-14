--->https://my.newtonschool.co/playground/code/1g9zy3z96hm9



# Your code here
n=int(input())
m=0
ans=0
for i in range(n) :
    w,q=map(int,input().split())
    if w <= 10 :
        if q >= m :
            m=q
            ans=i+1
print(ans) 
