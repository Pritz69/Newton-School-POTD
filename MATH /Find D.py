---->https://my.newtonschool.co/playground/code/g7vuoihsh2nb



# Your code here
a,b,c=map(int,input().split())
while a <= b :
    if a%c==0 :
        print(a)
        exit()
    a +=1
print(-1)
