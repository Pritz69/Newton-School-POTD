---->https://my.newtonschool.co/playground/code/hh0oxkw0mqrk



t = int(input())

for _ in range(t):
    n = int(input())
    occ = {}
    
    numbers = list(map(int, input().split()))
    for x in numbers:
        occ[x] = occ.get(x, 0) + 1
    
    if len(occ) >= 3:
        print("No")
    else:
        if abs(list(occ.values())[0] - list(occ.values())[-1]) <= 1:
            print("Yes")
        else:
            print("No")
