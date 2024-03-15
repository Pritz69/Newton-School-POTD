import math

# Read input values
a, b = map(int, input().split())

# Initialize counters
c = 0  # Counter for extension cords
s = 1  # Total number of sockets, initially set to A

# Loop until the total number of sockets is greater than or equal to B
while s < b:
    c += 1  # Increment the counter for extension cords
    s += (a - 1)  # Update the total number of sockets by adding A - 1

# Print the result
print(c)
