---->https://my.newtonschool.co/playground/code/4qnk9i2fah6m



# Your code here
n=int(input())
l=""
s=input()
for i in range(1,n) :
    if s[i-1] in "aeiouy" and s[i] in "aeiouy" :
        continue
    else :
        l += s[i-1]
l +=s[i]
print(l)
