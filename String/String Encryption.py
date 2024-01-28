---->https://my.newtonschool.co/playground/code/1paw8c7zx9y2



s = input().strip()
ns = ""
p = s[0]
c = 1
#d = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}
def decimal_to_hexadecimal(decimal_number):
    if decimal_number == 0:
        return "0"

    hex_digits = "0123456789abcdef"
    result = ""

    while decimal_number > 0:
        remainder = decimal_number % 16
        result = hex_digits[remainder] + result
        decimal_number //= 16

    return result
for i in range(1, len(s)):
    if s[i] == p:
        c += 1
    else:
        ns = ns + p
        ns = ns + decimal_to_hexadecimal(c)
        c = 1
        p = s[i]

ns = ns + p
ns = ns + decimal_to_hexadecimal(c)
print(ns[::-1])
