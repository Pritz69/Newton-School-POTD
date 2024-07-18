N=int(input())
A=list(map(int,input().split()))
    
M = min(A)  # Minimum value in the array A
    
count_greater_than_M = sum(1 for x in A if x > M)
count_already_100 = sum(1 for x in A if x == 100)
    
    # Minimum operations required
min_operations = count_greater_than_M 
    
print(min_operations)
