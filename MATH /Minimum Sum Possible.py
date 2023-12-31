-->https://my.newtonschool.co/playground/code/swnmsrp2v7x4



x,y,k=map(int,input().split())
def gcd(a,b) :
    if b==0 :
        return a
    return gcd(b,a%b)
def lcm(a,b) :
    ans=(a*b)
    ans=ans//gcd(a,b)
    return ans 
l=[x,y]
for i in range(k) :
    if l[0]>l[1] :
        l[0]=gcd(l[0],l[1])
    else :
        l[1]=gcd(l[0],l[1])
    if l[0]>l[1] :
        l[0]=lcm(l[0],l[1])
    else :
        l[1]=lcm(l[0],l[1])
#print(gcd(x,y))
#print(lcm(x,y))
print(sum(l))
