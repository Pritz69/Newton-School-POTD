def min_energy(n, m):
    # Upper limit for numbers (as per the problem statement)
    MAXN = 1000000
    
    # Step 1: Calculate smallest prime factors (SPF) for each number up to MAXN
    spf = list(range(MAXN + 1))  # smallest prime factor
    
    for i in range(2, int(MAXN**0.5) + 1):
        if spf[i] == i:  # i is a prime number
            for j in range(i * i, MAXN + 1, i):
                if spf[j] == j:
                    spf[j] = i
    
    # Step 2: Function to calculate number of distinct prime factors
    def num_distinct_prime_factors(x):
        distinct_factors = set()
        while x != 1:
            distinct_factors.add(spf[x])
            x //= spf[x]
        return len(distinct_factors)
    
    # Step 3: Calculate the total energy needed
    total_energy = 0
    for i in range(n, m ):
        total_energy += num_distinct_prime_factors(i)
    
    return total_energy

# Reading input
n, m = map(int, input().strip().split())

# Output the result
print(min_energy(n, m))
