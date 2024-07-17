# Your code here
n=int(input())
l=list(map(int,input().split()))
l2=list(map(int,input().split()))
c=0
for i in range(n) :
    if 2*l[i] < l2[i] :
        continue
    elif l[i] > 2*l2[i] :
        continue
    else: 
        c +=1
print(c) 
