--->https://my.newtonschool.co/playground/code/s4wyrcd7n4o8



# Your code here
n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(32) :
    f=0
    for j,v in enumerate(l) :
        if v>>i & 1==1:
            f +=1
    s += (f%3)<<i 
print(s)



#14 12 14 14 9 9 9

#16 8 4 2 1
#   1 1 1
#   1 1 1
#   1 1 1
#   1     1
#   1     1
#   1     1
#   1 1
