---->https://my.newtonschool.co/playground/code/ki94viglcp2a



def min_shovels(k, r):
    for i in range(1, 11):
        total_price = k * i
        if total_price % 10 == 0 or total_price % 10 == r:
            return i
    return 10  # If for loop completes without returning, it means Raj needs to buy at least 10 shovels

# Input
k, r = map(int, input().split())

# Output
print(min_shovels(k, r))



k,r = map(int, input().split())
i=1
while (k*i)%10!=r and (k*i)%10!=0 :
    i +=1
print(i)
