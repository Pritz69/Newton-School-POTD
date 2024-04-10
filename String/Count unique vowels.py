# Your code here
s=input()
se=set()
for x in s :
    if x in "aeiouAEIOU" :
        se.add(x)
print(len(se))
