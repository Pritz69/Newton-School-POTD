# Your code here
for i in range(int(input())):
    a,b=map(int,input().split())
    x=10**9+7
    # (2**a - 1)**b
    print(pow(( pow(2,a,x) - 1 ),b,x))
