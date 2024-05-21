# Python Implementation

import math

# Function to check whether the number is prime or not
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

# Function to calculate the number of prime factors
def prime_factors(n):
    ans = 0
    while n % 2 == 0:
        ans += 1
        n = n // 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            ans += 1
            n = n // i
    if n > 2:
        ans += 1
    return ans

# Function to determine which player will win
def brain_game(nums):
    a = [0] * 1005
    # Pre-compute the prime factors for numbers from 2 to 1000
    for i in range(2, 1001):
        if not is_prime(i):
            a[i] = prime_factors(i) - 1
    x = 0
    # Calculate XOR of prime factors for each number in nums
    for num in nums:
        x = x ^ a[num]
    # If XOR result is 0, player B wins; otherwise, player A wins
    if x == 0:
        return False
    return True

# Main function
n = int(input())
nums = list(map(int,input().split()))

# Check the winner and print the result
if brain_game(nums):
    print("A")
else:
    print("B")

# This code is contributed by Tapesh(tapeshdu420)
