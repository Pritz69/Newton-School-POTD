---->https://my.newtonschool.co/playground/code/mxd97i1aze71 


#CODING IT IN THE HARD WAY WITHOUT USING EXTRA SPACE

# Your code here
n=int(input())
l=list(map(int,input().split()))
x=0
for i in range(n) :
    x = x ^ l[i]
#print(x)
b=0
while x & 1 !=1 :
    x = x>>1
    b +=1
#print(x,b)
l1=[]
l2=[]
for x in l :
    if x>>b & 1 ==1 :
        l1.append(x)
    else :
        l2.append(x)
#print(l1,l2)
x1=0
x2=0
for x in l1 :
    x1=x1^x
for x in l2 :
    x2=x2^x 
ans=x1+x2 
print(ans)
