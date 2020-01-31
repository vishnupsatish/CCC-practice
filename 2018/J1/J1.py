numbers = [int(input()) for i in range(4)]
if (numbers[0] >= 8) and (numbers[3] >= 8) and (numbers[1] == numbers[2]):
    print("ignore")
else:
    print("answer")