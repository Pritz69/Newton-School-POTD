# Your code here
for _ in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    for x in b :
        a=a[:n-x] + sorted(a[n-x:])
    print (" ".join(str(x) for x in a))
