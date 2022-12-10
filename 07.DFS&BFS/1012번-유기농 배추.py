# DFS
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

T = int(input())

for _ in range(T):

    m, n, k = map(int, input().split())

    g = [[0]*(m) for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        g[y][x] = 1

    def DFS(x,y):
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]

            if 0<=a<n and 0<=b<m and g[a][b] == 1:
                g[a][b] = 0
                DFS(a,b)

    # 벌레 개수
    cnt = 0

    # DFS 호출
    for i in range(n):
        for j in range(m):
            if g[i][j] == 1:
                g[i][j] = 0
                DFS(i,j)
                cnt += 1

    print(cnt)
    

