# Your code here
for _ in range(int(input())) :
    n=int(input())
    l=list(map(int,input().split()))
    l.sort(reverse=True)
    s=set()
    for x in l :
        s.add(x)
        if len(s)==2 :
            break
    print(sum(x for x in s))
