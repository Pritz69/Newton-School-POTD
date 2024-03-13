# Your code here
n=int(input())
s=0
c=0
while n :
    if c==2 :
        break
    s += n%10
    n = n//10
    c +=1
print(s)
