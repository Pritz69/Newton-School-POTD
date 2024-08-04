from math import inf;
# ---------------------------------------- COLLECTIONS -----------------------------------------------#
from collections import defaultdict #"""using this, we can give a default value of data type to dict"""
from collections import OrderedDict #"""this stores the order of insertion of values in dict"""
from collections import Counter  #"""returns a dict containing count of values"""
from collections import ChainMap  #"""to have diff. dicts in one class (container)"""
#"""we have to use .new_child(new_dictToInsert) to insert a new dict into ChainMap"""
#---------------------------------------- COLLECTIONS ------------------------------------------------ #

def getlist():
    return list(map(int, input().split()))
    
def getinp():
    return map(int, input().split())
    
#----------------------------------------- MAIN CODE -------------------------------------------------#    
def main():
    for _ in range(int(input())):
        n ,k = getinp()
        s = input();
        if k == 1:
            print(0) if '1' in s else print(1)
        else:
            different = 0; prev = ''; pre = [0]*(n+1);
            for i in range(n):
                if prev:
                    if prev != s[i]:
                        different += 1; prev = s[i];
                else: prev = s[i];
                pre[i] = different;
            if n == k: 
                diff = pre[k-1] - pre[0];
                if s[k-1] == '0': diff += 1;
                print(diff);
            else:
                minn = pre[k-1] - pre[0];
                if s[k-1] == '0': minn += 1;
                for i in range(1, n):
                    if (k + i - 1) < n:
                        temp = pre[k+i-1] - pre[i];
                        if s[k+i-1] == '0': temp += 1;
                    minn = min(temp, minn);
                print(minn)
#----------------------------------------- MAIN CODE -------------------------------------------------#

if __name__ == "__main__":
    main()
