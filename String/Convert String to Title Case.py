s = input().strip()  # Take input and remove any leading or trailing whitespace
ns = []  # Initialize an empty list to store the modified words

# Split the input sentence into individual words and iterate through each word
for x in s.split(" "):
    if x.isupper():
        ns.append(x)  # If the word is entirely uppercase, append it as is
    else:
        # Capitalize the first letter and make the rest of the letters lowercase
        ns.append(x[0].upper() + x[1:].lower())

print(" ".join(ns))  # Join the list into a string with spaces and print
