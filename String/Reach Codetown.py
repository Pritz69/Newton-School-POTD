# Your code here
for i in range(int(input())) :
    s=input()
    if s=="CODETOWN" :
        print("No")
    else :
        f=0
        if s[0] in "AEIOU" :
            f=1
        if s[1] not in "AEIOU" :
            f=1
        if s[2] in "AEIOU" :
            f=1
        if s[3] not in "AEIOU" :
            f=1
        if s[4] in "AEIOU" :
            f=1
        if s[5] not in "AEIOU" :
            f=1
        if s[6] in "AEIOU" :
            f=1
        if s[7] in "AEIOU" :
            f=1
        if f==1 :
            print("No")
        else :
            print("Yes")
