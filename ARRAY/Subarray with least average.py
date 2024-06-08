n, k = map(int, input().split())
a = list(map(int, input().split()))
l, r = 0, 0
ans = 0
current_sum = 0
min_sum = float('inf')
while r < n:
    current_sum += a[r]
    if (r - l + 1) == k:
        if current_sum < min_sum:
            min_sum = current_sum
            ans = l
        current_sum -= a[l]
        l += 1
    r += 1
print(ans + 1)
