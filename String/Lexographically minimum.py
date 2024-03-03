---->https://my.newtonschool.co/playground/code/t4h3m01yoobb



# Your code here
n=int(input())
for i in range(1,27):
    f2=0
    for j in range(1,27) :
        f=0
        for k in range(1,27) :
            if i+j+k==n :
                f=1
                break
        if f==1 :
            f2=1
            break 
    if f2==1 :
        break 
ans=chr(96+i) + chr(96+j) + chr(96+k)
print(ans)
