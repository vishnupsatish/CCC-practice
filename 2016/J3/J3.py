word = input()
largest = 0
for i in range(len(word)):
    for j in reversed(range(len(word)+1)):
        new = word[i:j]
        #print(new)
        if new == new[::-1]:
            if len(new) > largest:
                largest = len(new)
                break
print(largest)
#print(word[0:4])