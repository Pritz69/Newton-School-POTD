# Your code here
n=int(input())
i=2
xor=0
while i <=n :
    if n%i==0 :
        xor=xor^i 
    i+=2
print(xor)
