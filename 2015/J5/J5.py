"""
Problem: CCC 2015 J5
Name: Vishnu Satish
Solution: Use recursion to find the
possible values for a sorted list with
length as the number of mathematicians
such that the elements sum to the number of pieces
"""


n = int(input())
k = int(input())

ans = 0


# A recursive function which accepts min, pieces, and people
def pi(pieces, people, min):
	global ans
	# If the number of people is
	# 1 and the current values
	# are possible, add one to answer
	if people == 1:
		ans += 1
		return
	# For every value from min (the previous value in the list)
	# to the maximum possible value, call the recursive function
	# while adding the current value for "i" to the list
	for i in range(min, pieces//people + 1):
		pi(pieces - i, people - 1, i)


# Call the function with the starting values, then
# once the function has ended, print the value of ans
pi(n, k, 1)
print(ans)
