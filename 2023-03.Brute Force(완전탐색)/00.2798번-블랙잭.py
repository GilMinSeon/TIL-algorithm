n, m = map(int, input().split())
card = list(map(int, input().split()))

pick_cnt = 3 # 3장의 카드를 골라야한다

res = [0]*(pick_cnt+1)
max_val = 0

def DFS(L, s):
    global max_val

    if L == pick_cnt:
        sum_val = sum(res)
        print(res)
        if sum_val <= m:
            if max_val < sum_val:
                max_val = sum_val
    else:
        for i in range(s, n):
            res[L+1] = card[i]
            DFS(L+1, i+1)

DFS(0, 0)

print(max_val)