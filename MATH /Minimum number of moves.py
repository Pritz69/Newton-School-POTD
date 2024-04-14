---->https://my.newtonschool.co/playground/code/9j0bb6q2cwft



def min_moves_to_reach_n(N):
    if N==1 :
        return 2
    if N%3==0 :
        return (N//3)
    return N//3 + 1

# Sample Input
N = int(input().strip())

# Output minimum number of moves
print(min_moves_to_reach_n(N))
