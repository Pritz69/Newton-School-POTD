# Your code here
for _ in range(int(input())):
    n,k=map(int,input().split())
    if k==0 and n%4==0 :
        print("Off")
    elif k==0 and n%4 != 0 :
        print("On")
    elif k==1 and (n==0 or n%4==0) :
        print("On")
    else :
        print("Ambiguous")
