n = int(input())
k = int(input())

ans = 0

# memo = [[[0 for _ in range(n//k)] for __ in range(n)] for ___ in range(k)]

# print(memo)


def pi(pieces, people, min):
	global ans
	if people == 1:
		ans += 1
		return
	for i in range(min, pieces//people + 1):
		pi(pieces - i, people - 1, i)


pi(n, k, 1)
print(ans)
