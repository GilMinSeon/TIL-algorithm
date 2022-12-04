import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
g = [[0]*(n+1) for _ in range(n+1)]
ch = [0]*(n+1)
dq = deque()
cnt = 0

for i in range(m):
    a, b = map(int, input().rstrip().split())
    g[a][b] = 1
    g[b][a] = 1

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print(g[i][j], end=' ')
#     print()

def BFS(v):
    global cnt

    ch[v] = 1
    dq.append(v)

    while dq:
        cnt += 1
        now = dq.popleft()
        #print(now, end=' ')

        for x in range(1, n+1):
            if g[now][x] == 1 and ch[x] == 0:
                ch[x] = 1
                dq.append(x)

BFS(1)

print(cnt-1)