'''
Author: Vishnu Satish
Problem: CCC 2017 J5
Algorithm: For every plank length, if the lengths are the same,
divide the number of planks with that length by two to get the number
of possible board lengths, or if the lengths are different, take the
minimum of the number of different lengths, to avoid over counting.
'''

# Get n from input and initialize two variables, used for plank length and board length
n = int(input())
l = [0] * 2001
b = [0] * 4002

lengths = list(map(int, input().split()))

# Add length in list for every plank length
for length in lengths:
    l[length] += 1

# Iterate over the lengths list
for i in range(len(l) - 1):

    # Iterate a second time, starting from the
    # current element's index from the first iteration
    for j in range(i, len(l)):
        # If they are the same plank length, integer
        # divide by two and add it to the board length list
        if i == j:
            b[i + j] += l[i] // 2
        # If not, take the min of both plank
        # lengths and add it to the board length list
        else:
            b[i + j] += min(l[i], l[j])

# This prints the max board length and the number of possibilities for the max board lengths
print(max(b), b.count(max(b)))
