def minimum_travel_time(n):
    c = 1  # Initial step count, since we start at the first subway station
    p = 1  # The first subway station at position 1
    i = 2  # The next triangular number addition

    # Find the maximum triangular number less than or equal to n
    f=0
    while p < n:
        if n-p <= (1+(p+i-n)) :
            f=1
            break
        p = p + i
        c += 1
        i += 1
    if f==1 :
        c += (n-p) 
    else :
        c += (p - n)
    
    # Compare walking the entire distance vs using the subway
    return min(c, n)

# Example usage
X = int(input())
print(minimum_travel_time(X))
