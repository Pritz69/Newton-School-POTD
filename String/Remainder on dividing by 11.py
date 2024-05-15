# Your code here
n=input()
ans=0
for i in range(len(n)) :
    ans=( (ans*10)+(int(n[i])) )%11
print(ans)
