# Your code here
n=int(input())
l=list(map(int,input().split()))
k=int(input())
ma,mi=float('-inf'),float('inf')
for x in l :
    ma=max(ma,x)
    mi=min(mi,x)
print(max(0,(ma-k)-(mi+k)) )
