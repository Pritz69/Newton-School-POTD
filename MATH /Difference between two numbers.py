---->https://my.newtonschool.co/playground/code/n78eohztb8a3



# Your code here
a,b,c=map(int,input().split())
if a==b-c or a==c-b or b==c-a or b==a-c or c==a-b or c==b-a :
    print("Yes")
else :
    print("No")
