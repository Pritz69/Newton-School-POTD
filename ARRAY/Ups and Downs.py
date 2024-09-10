def rearrange_elements(T, test_cases):
    results = []
    for _ in range(T):
        N = test_cases[_][0]
        A = test_cases[_][1]

        A.sort()  # Sort the array
        result = [0] * N
        left = 0           # Start from the smallest element
        right = N - 1      # Start from the largest element

        # Fill even indices with smaller elements, and odd indices with larger elements
        for i in range(N):
            if i % 2 == 0:
                result[i] = A[left]
                left += 1
            else:
                result[i] = A[right]
                right -= 1
        
        results.append(result)
    
    return results

# Reading input
T = int(input().strip())
test_cases = []
for _ in range(T):
    N = int(input().strip())
    A = list(map(int, input().strip().split()))
    test_cases.append((N, A))

# Calling function to get results
results = rearrange_elements(T, test_cases)

# Printing results
for result in results:
    print(" ".join(map(str, result)))
