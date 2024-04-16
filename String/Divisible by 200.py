---->https://my.newtonschool.co/playground/code/u2l4ojp1mfxe



# Your code here
n,k=map(int,input().split())
for i in range(k) :
    if n%200==0 :
        n=n//200
    else :
        n=int(str(n)+str(200))
print(n)
