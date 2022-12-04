import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

n, m = map(int, input().split())
g = [[0]*(n+1) for _ in range(n+1)]
ch = [0]*(n+1)
cnt = 0

for i in range(m):
    a, b = map(int, input().rstrip().split())
    g[a][b] = 1
    g[b][a] = 1

def DFS(v):
    # 일단 DFS 뻗었다는 뜻이니까 체크배열에 체크하기!
    ch[v] = 1
    
    # 가지뻗기
    for i in range(1, n+1):
        if g[v][i] == 1 and ch[i] == 0:
            DFS(i)

for i in range(1, n+1):
    if ch[i] == 0:
        DFS(i)
        cnt += 1

print(cnt)