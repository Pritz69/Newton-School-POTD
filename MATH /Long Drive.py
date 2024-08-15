# Your code here
for _ in range(int(input())) :
    x,y=map(int,input().split())
    d=10*x
    i=10
    while True :
        i +=1
        rd=i*y 
        if ((rd-d)/(i-10)) > 100 :
            continue
        else :
            break
    print(i-10)
