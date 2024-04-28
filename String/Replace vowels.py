# Your code here
n=int(input())
l=list(input())
for i in range(n) :
    if l[i]=='a' :
        l[i]='b'
    elif l[i]=='e' :
        l[i]='f'
    elif l[i]=='i' :
        l[i]='j'
    elif l[i]=='o' :
        l[i]='p'
    elif l[i]=='u' :
        l[i]='v'
    else :
        continue
print(''.join(l))
