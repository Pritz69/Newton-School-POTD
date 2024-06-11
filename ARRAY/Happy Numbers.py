# Your code here
n=int(input())
def findNth(n):
 
    # vector to store results
    ans = []
 
    # push first 6 numbers in the answer
    for i in range(6):
        ans.append(i)
 
    # calculate further results
    for i in range(n // 6 + 1):
        for j in range(6):
            if ((ans[i] * 10) != 0):
                ans.append(ans[i]
                           * 10 + ans[j])
 
    return ans[n - 1]
print(findNth(n))
