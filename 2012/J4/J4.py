change = int(input())
string = str(input())
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
newstring = ""
for i in range(len(string)):
    shiftValue =


'''
    j = i + 1
    shiftValue = 3 * j + change
    print(shiftValue)
    print(string[i])
    if alphabet.index(string[i]) + shiftValue > len(alphabet):
        shiftValue = shiftValue - (len(alphabet) - shiftValue)
    newstring += alphabet[shiftValue]
print(newstring)
'''