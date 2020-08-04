c1 = int(input())
c2 = int(input())
if c1 > 0 and c2 > 0:
    print(1)
elif c1 > 0 and c2 < 0:
    print(4)
elif c1 < 0 and c2 > 0:
    print(2)
elif c1 < 0 and c2 < 0:
    print(3)