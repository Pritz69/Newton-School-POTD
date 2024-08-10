# Your code here
for _ in range(int(input())) :
    n=int(input())
    if n%10 >= 5 :
        n += (10-(n%10))
    else :
        n -= n%10
    print(100-n)
