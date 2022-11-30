# BFS풀이
from collections import deque

# 8방향(상하좌우+대각선4방향)
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

# BFS할 큐 배열 준비
dq = deque()

# BFS 함수
def BFS():
    global cnt

    while dq:
        now = dq.popleft()

        for i in range(8):
            a = now[0] + dx[i]
            b = now[1] + dy[i]

            if 0<=a<h and 0<=b<w and board[a][b]==1:
                dq.append((a,b))
                board[a][b] = 0


while True:
    w, h = map(int, input().split())
    if (w,h) == (0,0): 
        break   # 종료조건
    board = [list(map(int, input().split())) for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] == 1:
                cnt += 1
                dq.append((i,j))
                board[i][j] = 0
                BFS()
    print(cnt)

