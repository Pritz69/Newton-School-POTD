--->https://my.newtonschool.co/playground/code/t3pm39xthjvm


TRICKY QUESTION


for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))

    running_sum = 0
    coins_needed = 0

    for i in range(n-1,-1,-1):
        running_sum += l[i]
        if running_sum > 0:
            coins_needed += running_sum
            running_sum = 0

    print(coins_needed)
