from math import ceil

N = int(input())

memo = {1: 1, 2: 1, 3: 2, 4: 3, 5: 4, 10: 13}


def determine(N):
    if N in memo:
        return memo[N]

    ans = 0
    ans += ceil(N / 2)

    for K in range(2, N // 2 + 1):
        correct_value = N // K
        ans += determine(correct_value)

    memo[N] = ans

    return ans


print(determine(N))
