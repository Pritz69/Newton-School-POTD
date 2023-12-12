-->https://my.newtonschool.co/playground/code/o7jtv6pjbaaz



# Your code here
n=int(input())
l=list(map(int,input().split()))
def count_subordinates(n, bosses):
    subordinates_count = [0] * (n + 1)
    tree = {}
    for i in range(2, n + 1):
        boss = bosses[i - 2]
        if boss not in tree:
            tree[boss] = []
        tree[boss].append(i)
    def dfs(node):
        count = 1  
        if node in tree:
            for subordinate in tree[node]:
                count += dfs(subordinate)
        subordinates_count[node] = count-1
        return count

    dfs(1)
    return subordinates_count[1:]

output1 = count_subordinates(n,l)
st=""
for x in output1:
    st += str(x) + " "
print(st)
