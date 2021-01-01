# Times out on last batch

needle = input()
haystack = input()

arr = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0,
       'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

ans = 0

for char in needle:
    arr[char] += 1

done = dict()

arr_now = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
           'n': 0,
           'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

current_string = haystack[0:len(needle)]

for char in current_string:
    arr_now[char] += 1

if arr == arr_now:
    done[current_string] = True
    ans += 1

for i in range(1, len(haystack) - len(needle) + 1):
    current_string = haystack[i:i + len(needle)]

    if current_string in done:
        arr_now[haystack[i - 1]] -= 1
        arr_now[current_string[-1]] += 1
        continue

    arr_now[haystack[i - 1]] -= 1
    arr_now[current_string[-1]] += 1

    if arr == arr_now:
        done[current_string] = True
        ans += 1

print(ans)
