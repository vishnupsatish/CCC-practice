input()

swifts = list(map(int, input().split()))
semaphores = list(map(int, input().split()))

sum_swifts = 0
sum_semaphores = 0

ans = 0

for i, swift in enumerate(swifts):
    semaphore = semaphores[i]
    sum_swifts += swift
    sum_semaphores += semaphore
    if sum_semaphores == sum_swifts:
        ans = i + 1

print(ans)
