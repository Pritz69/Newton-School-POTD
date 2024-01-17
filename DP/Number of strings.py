--->https://my.newtonschool.co/playground/code/fdjk5eju68q5



# Your code here
n=int(input())
l=[1]*(n+1)
for i in range(1,n+1) :
    l[i]=l[i-1]*3
print(l[n])
