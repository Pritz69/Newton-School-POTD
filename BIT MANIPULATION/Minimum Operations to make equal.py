# Your code here
a,b=map(int,input().split())
c=a&b
if a==b :
    print(0)
elif a==c or b==c :
    print(1)
else :
    print(2)
