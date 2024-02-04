--->https://my.newtonschool.co/playground/code/ar7i67yt8bdw



# Your code here
n,m=map(int,input().split())
c=0
for i in range(100) :
    for j in range(100) :
        if (i + j*j)== n and (j + i*i)==m :
            c +=1
print(c)
