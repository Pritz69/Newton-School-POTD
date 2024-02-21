---->https://my.newtonschool.co/playground/code/92bk8eig2xl4



# Your code here
s=input()
ns=""
sm=0
for x in s :
    if x in "0123456789" :
        sm += int(x)
    else :
        ns +=x 
ns=sorted(ns)
print("".join(ns)+str(sm))
