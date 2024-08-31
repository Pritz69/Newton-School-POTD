# Your code here
s=input()
ans=[s[0]]
for i in range(1,len(s)) :
    if ans and abs(ord(s[i])-ord(ans[-1]))==32 :
        ans.pop()
    else :
        ans.append(s[i])
print("".join(ans))
