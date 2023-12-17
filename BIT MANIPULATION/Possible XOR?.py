-->https://my.newtonschool.co/playground/code/g8sn7ayvn2ti

Check if n is even:
If n is even, we can choose three distinct numbers such that their XOR sums to n.
For example, let's say we choose a = 0, b = n/2, and c = n/2. The equation becomes (0 ⊕ n/2) + (n/2 ⊕ n/2) + (0 ⊕ n/2) = n/2 + 0 + n/2 = n.


# Your code here
import math
n=int(input())
if n%2==0:
    print("YES")
else :
    print("NO")
