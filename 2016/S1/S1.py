s1 = input()
s2 = input()

d1 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0,
     'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

d2 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0,
     'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

for elem in s1:
    d1[elem] += 1

ast = s2.count('*')

for elem in s2:
    if elem == '*':
        continue
    d2[elem] += 1

for k in d1:
    if d2[k] < d1[k] and ast != 0:
        while d2[k] != d1[k]:
            d2[k] += 1
            ast -= 1
            if ast == 0:
                break

print('A') if d1 == d2 else print('N')