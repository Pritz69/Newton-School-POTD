# Your code here
i = int(input())
b = bin(i)[2:]

# Find the previous power of two
m = '1' + '0' * (len(b) - 1)

# Find the next power of two
n = '1' + '0' * len(b)
#print(m,n)
# Convert binary strings to integers
m_int = int(m, 2)
n_int = int(n, 2)
if abs(i-n_int) < abs(i-m_int) :
    print(n_int)
else :
    print(m_int)
