--->https://my.newtonschool.co/playground/code/dd3vdmbqi2tn



# Your code here
n,k,l,c,d,p,nl,np=map(int,input().split())
milk=(k*l)//nl
lime=(c*d)
salt=p//np
ans=min(milk,lime,salt)
ans=ans//n
print(ans)
