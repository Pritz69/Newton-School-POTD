----> https://my.newtonschool.co/playground/code/pvx8gvfc9fzw



# Your code here
n=int(input())
c=0
for a in range(1,n//2 +1) :
    for b in range(1,n//a +1) :
        if a*b + a == n :
            #print(a,b)
            c +=1
print(c)
