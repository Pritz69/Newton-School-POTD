# Your code here
for _ in range(int(input())) :
    x,h=map(int,input().split())
    c=0
    s=0
    while s < h :
        if c < 5 :
            s += x//2
        else :
            s +=x 
        c +=1
    print(c)
