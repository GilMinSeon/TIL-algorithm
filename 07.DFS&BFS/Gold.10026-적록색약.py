# https://www.acmicpc.net/problem/10026

# 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램

# 적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다
# 크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 

from collections import deque

n = int(input())

board = [list(map(str, input())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
visited2 = [[0]*n for _ in range(n)]
dq = deque([])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
res = 0
res2 = 0

def BFS(check_color):
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == check_color and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                dq.append([nx, ny])

def BFS2(check_color):
    if check_color != 'B':
        check_color = ('R', 'G')
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] in check_color and visited2[nx][ny] == 0:
                visited2[nx][ny] = 1
                dq.append([nx, ny])
        
                
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            res += 1
            dq.append([i,j])
            BFS(board[i][j])

for i in range(n):
    for j in range(n):
        if visited2[i][j] == 0:
            res2 += 1
            dq.append([i,j])
            BFS2(board[i][j])

print(res, res2, end = ' ')