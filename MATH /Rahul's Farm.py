# Your code here
for i in range(int(input())) :
    n=int(input())
    c=0
    if n < 4 :
        print(1)
    else :
        d=n//4
        c += d
        n=n - (d*4)
        c += n//2
        print(c)
