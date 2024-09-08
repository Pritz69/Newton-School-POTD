def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = sum(arr[i] % 2 for i in range(k - 1))
    ans = 0
    for i in range(k - 1, n):
        cnt += arr[i] % 2
        ans += 1 if cnt != 0 else 0
        cnt -= arr[i - k + 1] % 2
    print(ans)

tc = int(input())
for _ in range(tc):
    solve()
