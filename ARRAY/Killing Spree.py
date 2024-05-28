# Your code here
from math import sqrt
def maxPeople(p) : 
    tmp = 0
    count = 0
    for i in range(1, int(sqrt(p)) + 1) :
        tmp = tmp + (i * i)
        if (tmp <= p) :
            count += 1
        else :
            break
    return count
p=int(input())
print(maxPeople(p))
