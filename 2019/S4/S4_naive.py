# Times out

import itertools

N, K = list(map(int, input().split()))
attr = list(map(int, input().split()))

days = N // K + 1

ans = 0

l1 = False

if N == 1:
    print(attr[0])
    l1 = True


perms = list(set(itertools.combinations(list(range(1, K + 1)) * days, days)))

# m = {}

for p in perms:
    if sum(p) != N:
        continue

    sections = []

    now = 0

    for i, e in enumerate(p):
        # if (i, e) in m:
        #     now += m[(i, e)]
        #     continue
        sections.append(max(attr[ now : now + e ]))
        now += e
        # m[(i, e)] = e

    ans = max(sum(sections), ans)


if not l1:
    print(ans)
