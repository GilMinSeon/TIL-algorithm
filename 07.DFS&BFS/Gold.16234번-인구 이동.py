from collections import deque
import sys

N, L, R = map(int, input().split()) #인구 차이가 L명 이상, R명 이하
board = [list(map(int, input().split())) for _ in range(N)]

bfs_board = [[0]*N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(xx, yy, idx):
    dq = deque([])
    dq.append([xx, yy])
    
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<N and 0<=ny<N and bfs_board[nx][ny] == 0:
                org, new = board[x][y], board[nx][ny]
                if L<=abs(org-new)<=R:
                    dq.append([nx, ny])
                    bfs_board[nx][ny] = idx

area_idx = 1
for i in range(N):
    for j in range(N):
        if bfs_board[i][j] == 0:
            bfs_board[i][j] = area_idx
            BFS(i, j, area_idx)
            # 하고나서 bfs 끝났을때 인구이동 하기
            area_idx += 1

for i in range(N):
    print(bfs_board[i])
