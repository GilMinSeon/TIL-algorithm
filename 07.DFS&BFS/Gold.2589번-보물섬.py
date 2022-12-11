# https://www.acmicpc.net/problem/2589

from collections import deque

n, m = map(int, input().split())
board = [list(map(str, input())) for _ in range(n)]

dq = deque([])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS():
    max_val = -2147000000
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 'L' and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                max_val = visited[nx][ny]
                dq.append([nx, ny])
    return max_val-1

res = -2147000000

for i in range(n):
    for j in range(m):
        visited = [[0]*m for _ in range(n)]
        if board[i][j] == 'L':
            # python3 최적화
            if 0<=i-1<n and 0<=i+1<n:
                if board[i-1][j] == 'L' and board[i+1][j] == 'L': continue
            if 0<=j-1<m and 0<=j+1<m:
                if board[i][j-1] == 'L' and board[i][j-1] == 'L': continue

            visited[i][j] = 1
            dq.append([i,j])
            res = max(BFS(), res)
print(res)
