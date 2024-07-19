# Your code here
xx=int(input())
l=input()
c,n=0,0
for x in l :
    if x=="C" :
        c +=2
    elif x=="N" :
        n +=2
if c > n :
    print(60*xx)
elif c < n :
    print(40*xx)
else :
    print(55*xx)
