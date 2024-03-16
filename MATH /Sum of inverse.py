# Your code here
n=int(input())
l=list(map(int,input().split()))
s=0
for x in l :
    s += 1/x
s=1/s
print('%.8f' % s)
