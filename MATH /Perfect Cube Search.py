--->https://my.newtonschool.co/playground/code/sxqtvkew6stk



import math
def largest_perfect_cube(n):
    # Find the cube root of n
    cube_root = math.ceil(n ** (1/3))

    # Iterate from the cube root down to 1
    for i in range(cube_root, 0, -1):
        cube = i ** 3
        if cube <= n:
            return cube

# Input
n = int(input())

# Output
result = largest_perfect_cube(n)
print(result)
