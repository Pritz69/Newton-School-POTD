--->https://my.newtonschool.co/playground/code/uajv79oh780b



# Your code here
from collections import Counter
n=input()
c=Counter(n)
f=0
ans=float('inf')
for x in "newton" :
    if x not in c :
        f=1
        break
    else :
        ans=min(ans,c[x])
print(ans)
