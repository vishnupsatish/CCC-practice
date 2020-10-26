q = int(input())
n = int(input())
l1 = [int(a) for a in input().split()]
l2 = [int(a) for a in input().split()]
l1 = sorted(l1)
l2 = sorted(l2)
sum = 0
if q == 2:
	l2 = list(reversed(l2))
for i, _ in enumerate(l1):
	sum += max(l1[i], l2[i])

print(sum)