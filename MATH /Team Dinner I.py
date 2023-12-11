-->https://my.newtonschool.co/playground/code/xyqji5sxbbws



def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def fair_distribution(n, prices):
    total_bill = sum(prices)
    
    if not is_prime(total_bill//3):
        contribution_per_person = total_bill / 7
        return round(contribution_per_person, 2)
    else:
        return 0

# Input
n = int(input())
prices = list(map(int, input().split()))

# Output
result = fair_distribution(n, prices)
print(result)
