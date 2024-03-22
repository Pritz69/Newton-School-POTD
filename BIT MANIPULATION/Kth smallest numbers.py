---->https://my.newtonschool.co/playground/code/eh8o05jkbdr7



def kth_smallest(k):
    # Convert k to binary
    binary = bin(k)[2:]
    
    # Replace all '1's with '2's
    kth_number = int(binary.replace('1', '2'))

    return kth_number

# Input
k = int(input().strip())

# Output
print(kth_smallest(k))
