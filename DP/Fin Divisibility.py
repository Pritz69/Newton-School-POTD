---->https://my.newtonschool.co/playground/code/n8kwun93o2a0



# Your code here
n=int(input())
a,b=0,1
c=2
s=0
while s <= 10000 :
    s=a+b
    if s%n==0 :
        print(c)
        exit()
    c +=1
    a=b
    b=s
print(-1)
