square = []
for i in range(4):
    square.append(input().split())
for i in range(len(square)):
    for elem in range(len(square[i])):
        square[i][elem] = int(square[i][elem])
row0 = square[0][0] + square[0][1] + square[0][2] + square[0][3]
row1 = square[1][0] + square[1][1] + square[1][2] + square[1][3]
row2 = square[2][0] + square[2][1] + square[2][2] + square[2][3]
row3 = square[3][0] + square[3][1] + square[3][2] + square[3][3]
col0 = square[0][0] + square[1][0] + square[2][0] + square[3][0]
col1 = square[0][1] + square[1][1] + square[2][1] + square[3][1]
col2 = square[0][2] + square[1][2] + square[2][2] + square[3][2]
col3 = square[0][3] + square[1][3] + square[2][3] + square[3][3]
print("magic" if row0 == row1 and row1 == row2 and row2 == row3 and row3 == col0 and col0 == col1 and col1 == col2 and col2 == col3 else "not magic")



