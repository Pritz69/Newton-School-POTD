import sys
sys.setrecursionlimit(10**9)

def can_decorate(n, x, y):
    min_large_needed = max(0, 2 * n - x)
    if min_large_needed <= 2 * n and min_large_needed <= x and 3 * (n - (x - min_large_needed) // 2) <= y:
        return "Yes"
    return "No"
for _ in range(int(input())):
    n, x, y = map(int, input().split())
    print(can_decorate(n, x, y))
