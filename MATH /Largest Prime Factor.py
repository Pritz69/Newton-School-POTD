--->https://my.newtonschool.co/playground/code/1wv4vvkkzmw8



# Your code here
n=int(input())
m=0
i=2
t=n
while i*i <=n :
    if t%i==0 :
        m=max(m,i)
        t=t//i 
    else :
        i +=1
if t>1 :
    m=max(m,t)
if t==n :
    print(n)
else :
    print(m)
