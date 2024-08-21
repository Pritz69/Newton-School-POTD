# Your code here
for i in range(int(input())) :
    a,b,c=map(int,input().split())
    for i in range(1,101) :
        if a%i != 0 and b%i != 0 and c%i !=0 :
            print(i)
            break
