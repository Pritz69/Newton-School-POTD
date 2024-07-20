# Your code here
l=list(map(int,input().split()))
ans=0
if (l[0]==l[2] or l[0]==l[3]) and (l[1]==l[2] or l[1]==l[3]) :
    ans =1
elif (l[0]==l[4] or l[0]==l[5]) and (l[1]==l[4] or l[1]==l[5]) :
    ans =2
else :
    ans=0
print(ans)
