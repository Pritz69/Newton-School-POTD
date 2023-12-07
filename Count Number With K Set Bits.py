-->https://my.newtonschool.co/playground/code/rc1ry9wqmpk1


def count_numbers_with_k_set_bits(N, K):
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        dp[i] = dp[i >> 1] + (i & 1)
    result = sum(1 for count in dp if count == K)
    return result


N, K = map(int, input().split())


print(count_numbers_with_k_set_bits(N, K))
