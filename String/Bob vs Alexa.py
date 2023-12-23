--->https://my.newtonschool.co/playground/code/q4kyf2xflodz



a=input()
b=input()
i,j=0,0
while i<len(a) and j < len(b) :
    if b[j]==a[i] :
        j +=1
    i +=1
if j==len(b) :
    print("Yes")
else :
    print("No")
