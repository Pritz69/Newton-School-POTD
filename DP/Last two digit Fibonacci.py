# Your code here
n=int(input())
def precomput(f):
    f.append(0)
    f.append(1)
    for i in range(2,300):
        f.append((f[i-1] + f[i-2]) % 100)   
def findLastDigit(f,n):
    return f[n%300]
f = list()
precomput(f)
print(findLastDigit(f,n))

#FIBONACCI SERIES STARTS REPEATING AFTER 300th TERM
