"""
Problem: CCC 2020 S4
Name: Vishnu Satish
Solution: Create a, b, and c sections where you count
the number of swaps that need to be made to make each
section "happy". Note: I attempted to brute-force this
problem, and I solved it myself for the a and b section
only, but I was having trouble solving it including "c"s
in the string, so I took some help from the DMOJ editorial:
https://dmoj.ca/problem/ccc20s4/editorial where I understood
how to solve this where a "c" was present in the original string.
"""

s = input().lower()

a_start = 0
b_start = s.count('a')

c_exists = False

if 'c' in s:
    c_start = s.count('b') + s.count('a')
    c_exists = True

ans = float('inf')


def get_slice(s, start, stop):
    if start <= stop:
        return s[start:stop]
    return s[start:] + s[:stop]


if not c_exists:
    for _ in range(len(s)):
        a_section = get_slice(s, a_start, b_start)

        b_section = get_slice(s, b_start, a_start)

        ans = min(b_section.count('a'), ans)

        a_start += 1
        a_start = a_start % len(s)

        b_start += 1
        b_start = b_start % len(s)

else:
    for __ in range(len(s)):
        a_section = get_slice(s, a_start, b_start)

        b_section = get_slice(s, b_start, c_start)

        c_section = get_slice(s, c_start, a_start)

        ans = min((c_section.count('b') + c_section.count('a') + max(a_section.count('b'), b_section.count('a'))), ans)

        a_start += 1
        a_start = a_start % len(s)

        b_start += 1
        b_start = b_start % len(s)

        c_start += 1
        c_start = c_start % len(s)

    c_start = s.count('a')
    b_start = s.count('c') + s.count('a')

    for __ in range(len(s)):
        a_section = get_slice(s, a_start, c_start)

        b_section = get_slice(s, b_start, a_start)

        c_section = get_slice(s, c_start, b_start)

        ans = min((c_section.count('b') + c_section.count('a') + max(a_section.count('b'), b_section.count('a'))), ans)

        a_start += 1
        a_start = a_start % len(s)

        b_start += 1
        b_start = b_start % len(s)

        c_start += 1
        c_start = c_start % len(s)

print(ans)
