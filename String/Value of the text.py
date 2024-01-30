--->https://my.newtonschool.co/playground/code/kwykkr59rfo9



# Your code here
n=int(input())
l=list(input().split())
m=0
for x in l :
    c=0
    for i in x :
        if 65 <= ord(i) <= 90 :
            c +=1
    m=max(m,c)
print(m)
