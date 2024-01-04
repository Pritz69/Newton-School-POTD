--->https://my.newtonschool.co/playground/code/s5c64ptevm09



# Your code here
from collections import defaultdict
n=int(input())
l=list(map(int,input().split()))
nl=sorted(l)
ans=""
d=defaultdict(list)
for i,x in enumerate(nl) :
    d[x].append(i)
for x in l :
    if len(d[x])==1 :
        ans +=str(d[x][0]) + " "
    else :
        ans +=str(d[x][0]) + " "
        d[x].pop(0)
print(ans.strip())
