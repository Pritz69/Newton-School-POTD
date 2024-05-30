# Your code here
x,y=map(int,input().split())
if y%x==0 :
    print(y//x-1)
else :
    print(y//x)
