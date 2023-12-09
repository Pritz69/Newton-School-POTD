--> https://my.newtonschool.co/playground/code/au70pb1kw6j5



# Your code here
n=int(input())
st=""
while n > 0 :
    st = str(n%2) + st
    n =n//2
print(1<<(len(st)-1))
