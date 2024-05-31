# Your code here
import math
x,y,k=map(int,input().split())
ans=0
if y==x :
    ans=0
elif y > x :
    ans = int(math.ceil((y-x)/k))
else :
    ans =int(math.ceil((x-y)/k))
print(ans)
