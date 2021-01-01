
times = []

for _ in range(int(input())):
    time, dist = list(map(int, input().split()))
    times.append((time, dist))

times = sorted(times, key=lambda x: x[0])

ans = 0

for i, t in enumerate(times[1:]):
    ans = max(abs(t[1] - times[i][1])/(t[0] - times[i][0]), ans)

print(ans)