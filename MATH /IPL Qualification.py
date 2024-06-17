def min_wins_to_qualify(X, Y):
    return max(0, X - Y)

# Reading input
X, Y = map(int, input().strip().split())

# Output the result
print(min_wins_to_qualify(X, Y))
