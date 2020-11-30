P = int(input())
N = int(input())
R = int(input())
counter = N
days = 0
while counter <= P:
    N = N * R
    counter = counter + N
    days += 1
print(days)
