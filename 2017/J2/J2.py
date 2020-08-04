n = int(input())
new = n
k = int(input())
for i in range(1, k + 1):
    new += n * (10 ** i)
print(new)