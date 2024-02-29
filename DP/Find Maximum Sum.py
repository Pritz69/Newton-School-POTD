---->https://my.newtonschool.co/playground/code/74zbqhcqoke4



# Your code here
n=int(input())
def rec(n) :
    if n<12 :
        return n
    return max(n, max(rec(n//2),n//2) + max(rec(n//3),n//3) + max(rec(n//4),n//4))

ans=rec(n)
print(ans)
