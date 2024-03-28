---->https://my.newtonschool.co/playground/code/848k5ajr9vgl



# Your code here
n=int(input())
s=0
t=n
while n :
    s += n%10
    n = n//10
#print(s)
print("Yes" if t%s==0 else "No")
