---->https://my.newtonschool.co/playground/code/yo69nv32ue37



# Your code here
n=int(input())
l=[]
for i in range(1,n+1) :
    if n%i==0 and i <= n//i :
        l.append((i,n//i))
#print(l)
a,b=0,0
m=float('inf')
for x in l :
    if x[1]-x[0] < m :
        m=x[1]-x[0]
        a=x[0]
        b=x[1]
print(a,b)
