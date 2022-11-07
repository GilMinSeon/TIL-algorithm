def DFS(L):
    global cnt
    if L == n:
        if cnt == 1:
            for j in range(L):
                print(res[j], end = ' ')
            cnt = 2

        if res == a:
            cnt = 1

    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = i
                DFS(L+1)
                ch[i] = 0

n = int(input())
a = list(map(int, input().split()))
res = [0]*n

cnt = 0

ch = [0]*(n+1)
DFS(0)

if cnt == 1: print(-1)