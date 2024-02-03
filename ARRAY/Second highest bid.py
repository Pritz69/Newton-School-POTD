--->https://my.newtonschool.co/playground/code/ukbfpizmvnrf



# Your code here
n=int(input())
l=list(map(int,input().split()))
ans=[]
for i,v in enumerate(l) :
    ans.append((i,v))
ans=sorted(ans,key=lambda x:x[1])
print(' '.join([str(ans[-1][0]+1),str(ans[-2][1])]))
