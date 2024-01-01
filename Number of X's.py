--->https://my.newtonschool.co/playground/code/z21gi94u6eyu



# Your code here
l,r,x=map(int,input().split())
c=0
for i in range(l+1,r) :
    v=str(i)
    cnt=v.count(str(x))
    c+=cnt
print(c)
