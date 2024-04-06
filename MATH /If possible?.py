def has_common_factor(l, r):
    # Function to check if any number in the range [l, r] has a divisor other than 1
    for i in range(l, r + 1):
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                return True
    return False

def possible_numbers(l, r):
    # Check if any number in the range [l, r] has a divisor other than 1
    if has_common_factor(l, r):
        return "Yes"
    else:
        return "No"

# Input
l, r = map(int, input().split())

# Output
print(possible_numbers(l, r))
