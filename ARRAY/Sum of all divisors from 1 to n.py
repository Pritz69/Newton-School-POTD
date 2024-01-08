--->https://my.newtonschool.co/playground/code/85axmk35fdeh



# Your code here
def sum_of_divisors(n):
    result = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            result[j] += i

    return sum(result)
    
n = int(input())
print(sum_of_divisors(n))
