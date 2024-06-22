# Your code here
x,y,z=map(int,input().split())
if x<y and x<z :
    print("NOTHING")
elif x >= y :
    print("PIZZA")
elif x >=z :
    print("BURGER")
