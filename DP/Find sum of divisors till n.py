def sum_of_divisors(n):
    div_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            div_sum[j] += i
    #print(div_sum)
    return sum(div_sum)

n = int(input())
print(sum_of_divisors(n))
