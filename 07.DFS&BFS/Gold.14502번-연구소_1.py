from collections import deque
import sys, copy

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 안전영역 개수 구하기
def BFS():
    global max_val
    board1 = copy.deepcopy(board)# board를 변형시키면 안된다! 
    # 바이러스가 2니까 상하좌우 돌면서 2로 갈 수 있는거 다 간 다음에 BFS 끝나면 0인 개수 세주기
    dq = deque([])

    for i in range(n):
        for j in range(m):
            if board1[i][j] == 2:
                dq.append([i,j])

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<n and 0<=ny<m and board1[nx][ny] == 0:
                board1[nx][ny] = 2
                dq.append([nx, ny])

    # while문 끝났으면 개수 세주고 max_val 갱신
    tmp_cnt = 0
    for i in range(n):
        for j in range(m):
            if board1[i][j] == 0:
                tmp_cnt += 1

    max_val = max(max_val, tmp_cnt)

# DFS로 벽을 세우는 모든 경우의 수 계산
def DFS(L, x, y):
    if L == 3:
        # BFS 수행
        BFS()
    else:
        for i in range(x, n):
            for j in range(y if i==x else 0, m):
                if board[i][j] == 0:
                    board[i][j] = 1
                    DFS(L+1, i, j)
                    board[i][j] = 0

# 안전영역 정답변수
max_val = -2147000000

DFS(0, 0, 0)

print(max_val)