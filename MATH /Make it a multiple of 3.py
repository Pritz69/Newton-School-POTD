def min_digits_to_erase(N):
    digits = list(map(int, str(N)))
    k = len(digits)
    sum_digits = sum(digits)
    
    # Calculate remainder when sum of digits is divided by 3
    remainder = sum_digits % 3
    
    if remainder == 0:
        return 0  # No digits need to be erased
    
    # Greedily try to remove the minimum number of digits to make the sum divisible by 3
    found = False
    min_deletions = float('inf')
    
    # Try removing 1 to k-1 digits
    for num_erase in range(1, k):
        for i in range(k):
            if (sum_digits - digits[i]) % 3 == remainder:
                min_deletions = min(min_deletions, num_erase)
                found = True
        if found:
            break
        # Remove combinations of two digits
        for i in range(k):
            for j in range(i + 1, k):
                if (sum_digits - digits[i] - digits[j]) % 3 == remainder:
                    min_deletions = min(min_deletions, num_erase)
                    found = True
        if found:
            break
    
    if found:
        return min_deletions
    else:
        return -1

# Reading input
N = input().strip()
result = min_digits_to_erase(N)
print(result)
