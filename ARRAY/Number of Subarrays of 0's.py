--->https://my.newtonschool.co/playground/code/vemms9jsgkty



# Your code here
n=int(input())
l=list(map(int,input().split()))
c=1
ans=0
for i in range(1,n) :
    if l[i]==l[i-1] and l[i]==0 :
        c +=1
    else:
        ans += c*(c+1)//2
        if l[i]==0:
            c=1
        else :
            c=0
ans += c*(c+1)//2
print(ans)
