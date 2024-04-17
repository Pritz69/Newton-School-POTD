---->https://my.newtonschool.co/playground/code/v73kuw47fpu7



# Your code here
a,b=map(int,input().split())
a=str(a)
b=str(b)
i=len(a)-1
j=len(b)-1
f=0
while i >=0 and j >=0 :
    if int(a[i])+int(b[j]) >= 10 :
        f=1
        break
    i -=1
    j -=1
if f==1 :
    print("Yes")
else :
    print("No")
