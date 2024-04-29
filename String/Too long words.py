# Your code here
for i in range(int(input())) :
    s=input().strip()
    if len(s) <= 10 :
        print(s)
    else :
        n=len(s)
        #print(n)
        ans=s[0]+str(n-2)+s[n-1]
        print(ans)
