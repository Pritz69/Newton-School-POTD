def largest_number_possible(n, s):
    # If n is 1 and s is 0, the largest number would be 0
    if n == 1 and s == 0:
        return "0"
    # If n is greater than or equal to 2 and s is 0, it's not possible to form the number
    elif n >= 2 and s == 0:
        return "-1"
    
    # Initialize an empty string to store the largest number
    largest_number = ""

    # Iterate through each digit position
    for i in range(n):
        # If remaining sum is greater than or equal to 9, put 9 at current position
        if s >= 9:
            largest_number += "9"
            s -= 9
        # If remaining sum is less than 9, put the remaining sum at current position
        else:
            largest_number += str(s)
            s = 0

    # If after distributing digits, there's still a remaining sum, it's not possible to form the number
    if s > 0:
        return "-1"
    else:
        return largest_number

# Read input
n, s = map(int, input().split())

# Print the result
print(largest_number_possible(n, s))
