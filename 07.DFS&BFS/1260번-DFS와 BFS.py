from collections import deque
import sys


n, m, v = map(int, input().split())
g = [[0]*(n+1) for _ in range(n+1)]
ch = [0]*(n+1)
ch2 = [0]*(n+1)
dq = deque()

for i in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    g[a][b] = 1
    g[b][a] = 1

def DFS(v):
    print(v, end=' ')
    ch[v] = 1
    
    for i in range(1, n+1):
        if g[v][i] == 1 and ch[i] == 0:
            DFS(i)

def BFS(v):
    dq.append(v)
    ch2[v] = 1

    while dq:
        now = dq.popleft()
        print(now, end=' ')

        for i in range(1, n+1):
            if g[now][i] == 1 and ch2[i] == 0:
                dq.append(i)
                ch2[i] = 1

DFS(v)
print()
BFS(v)
