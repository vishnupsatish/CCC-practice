from math import sqrt


def is_prime(num):
    for c in range(2, int(sqrt(num)) + 1):
        if num // c == num / c:
            return False
    return True


nums = []

for _ in range(int(input())):
    nums.append(int(input()))

for num in nums:
    if is_prime(num):
        print(f'{num} {num}')
        continue
    n1 = num
    n2 = num
    while True:
        n1 += 1
        n2 -= 1
        if is_prime(n1) and is_prime(n2):
            break

    print(f'{n1} {n2}')
