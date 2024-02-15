---->https://my.newtonschool.co/playground/code/7iz3bjvm5pak



# Your code here
n=int(input())
s=input()
ans=len(s)-1
for j in range(len(s)):
    if s[j]=='B' :
        ans -=1
    else :
        break
for j in range(len(s)-1,-1,-1):
    if s[j]=='A' :
        ans -=1
    else :
        break
if ans <0 :
    print(max(ans,0))
else :
    print(ans)
