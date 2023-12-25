--->https://my.newtonschool.co/playground/code/27r191z32qr1



# Your code here
n=int(input())
s,c=n,0
while s != 0 :
    if s%2 ==0 :
        s //=2
        c +=1
    else :
        s -=1
        c +=1
print(c)
