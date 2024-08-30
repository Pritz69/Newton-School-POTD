# Your code here
for i in range(int(input())) :
    ra,ri=map(int,input().split())
    c=0
    while ra < (ri+10) :
        ra += 3
        c +=1
    print(c)
