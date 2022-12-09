import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
#g = [[0]*(n+1) for _ in range(n+1)]
g = [[] for _ in range(n+1)]
ch = [0]*(n+1)
dq = deque()

for i in range(m):
    a, b = map(int, input().rstrip().split())
    #g[a][b] = 1
    g[a].append(b)

print(g)

def BFS(v):
    global cnt

    ch[v] = 1
    dq.append(v)

    while dq:
        now = dq.popleft()
        for x in g[now]:
            if ch[x] == 0:
                ch[x] = ch[now] + 1
                dq.append(x)

# BFS호출
BFS(x)

# 출력
if k+1 not in ch:
    print(-1)
else:
    for i in range(1, n+1):
        if ch[i] == k+1:
            print(i)