# Your code here
c=0
x,y=map(int,input().split())
while x!=y :
    if x>y :
        x =x//2
    else :
        y =y//2
    c +=1
print(c)
