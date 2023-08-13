T = int(input())

for j in range(T):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    if len(arr) == 1:
        print(1)
        continue

    res = []
    for x in enumerate(arr):
        res.append(x)

    order = 1

    while True:
        idx, val = res.pop(0)
        if val >= max(arr):
            if idx == m:
                print(order)
                break
            else:
                order += 1
            arr[idx] = 0    # arr에서 해당 idx 점수 지우기
        else:
            res.append((idx, val))


