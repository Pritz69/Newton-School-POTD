---->https://my.newtonschool.co/playground/code/ty4ihe2ukfjb



# Your code here
def isprime(n) :
    for i in range(2,int(n**0.5)+1) :
        if n%i == 0 :
            return 0
    return 1
n=int(input())
while not isprime(n) :
    n +=1
print(n)
