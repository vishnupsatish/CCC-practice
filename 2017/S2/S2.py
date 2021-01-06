N = int(input())

odd = N % 2 != 0

tides = list(map(int, input().split()))

tides.sort()

low = []
high = []

if odd:
    low = list(reversed(tides[:N // 2 + 1]))
    high = tides[N // 2 + 1:]
else:
    low = list(reversed(tides[:N // 2]))
    high = tides[N // 2:]

for i in range(0, N // 2):
    print(low[i], end=' ')
    print(high[i], end=' ')

if odd:
    print(low[-1])




