# Your code here
for i in range(int(input())) :
    n=int(input())
    arr=list(map(int,input().split()))
    prefix_sum = 0
    first_occurrence = {0: -1}  
    max_length = 0
        
    for i in range(n):
        prefix_sum += arr[i]
        parity = prefix_sum % 2
            
        if parity in first_occurrence:
            length = i - first_occurrence[parity]
            max_length = max(max_length, length)
        else:
            first_occurrence[parity] = i
        
    print(max_length)
