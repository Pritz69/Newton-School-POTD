import math

def derangement(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return math.floor(math.factorial(n) / math.e + 0.5)

# Sample Input
N = int(input().strip())

# Calculate and print the result
print(derangement(N))
