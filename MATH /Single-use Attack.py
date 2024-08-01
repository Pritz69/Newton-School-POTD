# Your code here
for _ in range(int(input())):
    h,x,y=map(int,input().split())
    c=1
    h -=y 
    while h > 0 :
        h -=x
        c +=1
    print(c)
