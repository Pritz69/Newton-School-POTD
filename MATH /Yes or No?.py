---->https://my.newtonschool.co/playground/code/sx09t64qlur8



# Your code here
def min_divisor(n):
    for d in range(2, round(n ** 0.5) + 1):
        if n % d == 0:
            return d
    return n
 
l, r = map(int, input().split())
for x in range(l, r + 1):
    md = min_divisor(x)
    if md != x:
        print("Yes")
        break
else:
    print("No")
