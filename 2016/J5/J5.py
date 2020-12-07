"""
Problem: CCC 2016 J5
Name: Vishnu Satish
Solution: Sort both of the lists then reverse the
second list if they are asking for the maximum total
speed, then iterate over the first list and take
the max of that element and the corresponding element
in the second list
"""

q = int(input())
n = int(input())
l1 = [int(a) for a in input().split()]
l2 = [int(a) for a in input().split()]
l1 = sorted(l1)
l2 = sorted(l2)
sum_ = 0

if q == 2:
	l2 = list(reversed(l2))
for i, _ in enumerate(l1):
	sum_ += max(l1[i], l2[i])

print(sum_)