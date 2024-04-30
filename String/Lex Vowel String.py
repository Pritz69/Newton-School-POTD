# Your code here
s=input()
d={}
for x in s :
    d[x]=d.get(x,0)+1
ans=""
for x in "aeiou" :
    if x in d :
        ans += x*d[x]
print(ans)

