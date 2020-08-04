import re

subs = []
for _ in range(3):
    subs.append(input().split())
steps, start, end = input().split()
steps = int(steps)

def get_all_subs(_start):
    all_subs = []
    sub_indexes = []
    for elem in subs:
        sub_indexes.append([m.start() for m in re.finditer(f'(?={elem[0]})', _start)])
    for i in range(3):
        for index in sub_indexes[i]:
            #new_string = _start[index:len(subs[i][0]) + 1]
            new_string = _start[0:index] + subs[i][1] + _start[len(subs[i][0]) + index:]
            all_subs.append([new_string, i + 1, index + 1])
    return all_subs

done = False


def main(string, detail_steps, current_steps=0):
    global done
    if done:
        return
    all_subs = get_all_subs(string)
    if current_steps == steps and end == string:
        for elem in detail_steps:
            print(" ".join(elem))
        done = True
        return
    elif current_steps >= steps:
        return
    _steps = detail_steps
    for elem in all_subs:
        _steps = detail_steps
        if current_steps < steps:
            _steps.append([str(elem[1]), str(elem[2]), elem[0]])
            main(elem[0], _steps, current_steps=current_steps+1)
            _steps.pop()


main(start, [])