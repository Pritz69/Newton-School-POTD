---->https://my.newtonschool.co/playground/code/3litg7v9vf8n



n, k = map(int, input().split())
if n < k*k :
    print("NO")
elif n%2==0 and k%2==1 :
    print("NO")
elif n%2==1 and k%2==0 :
    print("NO")
else :
    print("YES")
