def count_groups(arr):
    count0, count1, count2 = 0, 0, 0
    
    for num in arr:
        if num % 3 == 0:
            count0 += 1
        elif num % 3 == 1:
            count1 += 1
        else:
            count2 += 1
    
    # Calculate pairs
    pairs = (count0 * (count0 - 1) // 2) + (count1 * count2)
    
    # Calculate triplets
    triplets = (count0 * (count0 - 1) * (count0 - 2) // 6) + \
               (count1 * (count1 - 1) * (count1 - 2) // 6) + \
               (count2 * (count2 - 1) * (count2 - 2) // 6) + \
               (count0 * count1 * count2)
    
    return pairs + triplets

# Input reading
n = int(input())
arr = list(map(int, input().split()))

# Output the result
print(count_groups(arr))
