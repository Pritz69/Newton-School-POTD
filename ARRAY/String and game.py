---->https://my.newtonschool.co/playground/code/wt8qs8jeii1o



# Your code here
import heapq
s=input().strip()
k=int(input())
d={}
for x in s :
    d[x]=d.get(x,0)+1
d=dict(sorted(d.items(),key=lambda x:x[1],reverse=True))
h=[]
for x in d :
    h.append(-d[x])
heapq.heapify(h)
#print(d)
#print(h)
while k  :
    x=heapq.heappop(h)
    x +=1
    k -=1
    heapq.heappush(h,x)
ans=0
for x in h :
    ans += x*x
print(ans)
