---->https://my.newtonschool.co/playground/code/9mfnhw0cs76w



# Your code here
i,j=0,0
x,k=map(int,input().split())
s=input()
f=0
for c in s :
    if c=='U' :
        j +=1
    elif c=='D' :
        j -=1
    elif c=='L' :
        i -=1
    else :
        i +=1
    if i==x and j==k :
        f=1
        break
if f==1 :
    print("YES")
else :
    print("NO")
