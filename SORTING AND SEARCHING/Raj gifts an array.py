---->https://my.newtonschool.co/playground/code/a4pcc4v1z4ih



# Your code here
n=int(input())
l=list(map(int,input().split()))
l.sort()
i,j=0,n-1
ans=0
#while i < j :
#    ans += l[j]-l[i]
#    i +=1
#    j -=1
for i in range(1,n) :
    ans += l[i]-l[i-1]
print(ans)
