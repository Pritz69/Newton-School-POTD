for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a.sort()
    b.sort(reverse=True)
    
    # Create the result arrays D and E
    d = a.copy()
    e = b.copy()
    
    # Check if the sum of corresponding elements are equal
    target_sum = d[0] + e[0]
    possible = True
    for i in range(1, n):
        if d[i] + e[i] != target_sum:
            possible = False
            break
    
    if possible:
        print(" ".join(map(str, d)))
        print(" ".join(map(str, e)))
    else:
        print(-1)
