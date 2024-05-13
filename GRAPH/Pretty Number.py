https://my.newtonschool.co/playground/code/3d46zof473gd



# A Python3 program to find all the Stepping Number from N=n
# to m using BFS Approach

# Prints all stepping numbers reachable from num
# and in range [n, m]
def bfs(n, m, num) :

	# Queue will contain all the stepping Numbers
	q = []
	q.append(num)
	while len(q) > 0 :
	
		# Get the front element and pop from the queue
		stepNum = q[0]
		q.pop(0);

		# If the Stepping Number is in the range
		# [n, m] then display
		if (stepNum <= m and stepNum >= n) :
			l.append(stepNum)

		# If Stepping Number is 0 or greater than m,
		# no need to explore the neighbors
		if (num == 0 or stepNum > m) :
			continue

		# Get the last digit of the currently visited
		# Stepping Number
		lastDigit = stepNum % 10

		# There can be 2 cases either digit to be
		# appended is lastDigit + 1 or lastDigit - 1
		stepNumA = stepNum * 10 + (lastDigit- 1)
		stepNumB = stepNum * 10 + (lastDigit + 1)

		# If lastDigit is 0 then only possible digit
		# after 0 can be 1 for a Stepping Number
		if (lastDigit == 0) :
			q.append(stepNumB)

		#If lastDigit is 9 then only possible
		#digit after 9 can be 8 for a Stepping
		#Number
		elif (lastDigit == 9) :
			q.append(stepNumA)

		else :
			q.append(stepNumA)
			q.append(stepNumB)

# Prints all stepping numbers in range [n, m]
# using BFS.
def displaySteppingNumbers(n, m) :

	# For every single digit Number 'i'
	# find all the Stepping Numbers
	# starting with i
	for i in range(10) :
		bfs(n, m, i)

		# Driver code
n, m = 0, int(input())

# Display Stepping Numbers in the
# range [n,m]
l=[]
displaySteppingNumbers(n, m)
l.sort()
print(l[-1])
