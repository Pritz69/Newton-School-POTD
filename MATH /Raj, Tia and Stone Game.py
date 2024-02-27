---->https://my.newtonschool.co/playground/code/lqr2u8zwtplx



# Your code here
def gcd(x,y) :
    if y==0 :
        return x
    return gcd(y,x%y)
#print(gcd(3,9))
a,b,n=map(int,input().split())
while True :
    if n<=0 :
        print("1")
        exit()
    t=gcd(a,n)
    n -=t
    #print(n)
    if n <=0 :
        print("0")
        exit()
    t2=gcd(b,n)
    n -=t2 
    #print(n)
