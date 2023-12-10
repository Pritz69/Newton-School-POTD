-->https://my.newtonschool.co/playground/code/8uddo24k1kgc



def find_nums(l, r):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    for a in range(2, r):
        b = r - a
        if l <= a + b <= r and gcd(a, b) != 1:   # if gcd(a, b) > 1:
            return "Yes"
    
    return "No"

l,r=map(int,input().split())
print(find_nums(l,r))
