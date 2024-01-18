--->https://my.newtonschool.co/playground/code/4x6roxd5vhym



# Your code here
n=int(input())
l=list(map(int,input().split()))
s1=0
s2=0
for i in range(0,n,2) :
    s1 += l[i]
for j in range(1,n,2) :
    s2 += l[j]
print(max(s1,s2))
