# Times out. how do I optimize this??????

N, K = list(map(int, input().split()))
attr = list(map(int, input().split()))

days = N // K + 1

ans = 0

memo = {}


def recur(new_attr: list, remain=K, ans_so_far=0, times=1):
    global ans
    if not new_attr:
        ans = max(ans, ans_so_far)
        return ans_so_far

    if times == days:
        if len(new_attr) > K:
            return
        recur([], ans_so_far=ans_so_far + max(new_attr))
        return

    for i in reversed(range(1, remain + 1)):
        if (tuple(new_attr[i:]), remain) in memo:
            now_ans = memo[(tuple(new_attr[i:]), remain)]
        else:
            now_ans = max(new_attr[:i])
            memo[(tuple(new_attr[i:]), remain)] = now_ans

        if len(new_attr[i:]) < K:
            recur(new_attr[i:], remain=len(new_attr[i:]), ans_so_far=ans_so_far + now_ans, times=times + 1)
        else:
            recur(new_attr[i:], ans_so_far=ans_so_far + now_ans, times=times + 1)


recur(attr)

print(ans)
