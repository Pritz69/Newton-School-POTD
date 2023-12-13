--> https://my.newtonschool.co/playground/code/f709j40e85ry



# Your code here
# Your code here
for i in range(int(input())) :
    n,k=map(int,input().split())
    l=[]
    s=set()
    i=1
    while i<=n and i!=k :
        if k-i <=n :
            if i not in s :
                l.append(i)
                s.add(i)
            if k-i not in s :
                s.add(k-i)
                l.append(k-i)
        i +=1
    for i in range(k,n+1):
        l.append(i)
    st=""
    for x in l :
        st += str(x) +" "
    if len(l)!=n:
        print(-1)
    else:
        print(st)
