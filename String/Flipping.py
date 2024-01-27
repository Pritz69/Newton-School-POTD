--->https://my.newtonschool.co/playground/code/k03ap7g0v3f9



# Your code here
n=int(input())
s=input()
l=list(s)
c=0
vis=set()
#print(l)
if l[0]=='B' and l[-1]=='A' :
    print(0)
else :
    f=1
    while len(vis) != n-1 and f==1:
        f=0
        for i in range(n-1) :
            if l[i]=='A' and l[i+1]=='B' and i not in vis :
                f=1
                l[i],l[i+1]=l[i+1],l[i]
                c +=1
                #print(l,c)
                vis.add(i)
    print(c)
