# https://www.acmicpc.net/problem/7576

# 하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 방향이다
# 며칠이 지나야 모든 토마토가 익을 수 있는가?

# 정수 1은 익은 토마토,
# 정수 0은 익지 않은 토마토,
# 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.

# M 가로(col) / N 세로(row)

from collections import deque

M, N = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(N)]
queue = deque([])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
res = 0

for i in range(N):
    for j in range(M):
        if data[i][j] == 1:
            queue.append([i, j])

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < N and 0 <= ny < M and data[nx][ny] == 0:
                data[nx][ny] = data[x][y] + 1
                queue.append([nx, ny])
                
bfs()

for i in data:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))

print(res - 1)



'''
from collections import deque
import sys

# 4방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 문제의 input
m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 최종답
res_day = 0

# BFS
def BFS():
    global res_day
    while Q:
        tmp = []
        for k in range(len(Q)):
            tmp.append(Q.popleft())

        for x in tmp:
            now = x
            for i in range(4):
                a = now[0] + dx[i]
                b = now[1] + dy[i]

                if 0<=a<n and 0<=b<m and board[a][b] != 1 and board[a][b] != -1:
                    Q.append((a,b))
                    board[a][b] = 1
        res_day += 1

# 답 체크
flag = True
for i in range(n):
    for j in range(m):
        if board[i][j] == -1: continue
        if board[i][j] == 0: flag = False

if flag == True:
    print(0)
else:
    # 값이 없을때까지 돌릴 큐 하나 만들어서 거기다가 첫번째 값 넣어두기
    Q = deque()
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                Q.append((i,j))
    # BFS 호출
    BFS()
    flag2 = True
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                print(-1)
                flag2 = False
                sys.exit(0)#........ 제발 ㅠㅠㅠㅠㅠ 이런거 어떻게 해야해 진짜~~~~ ㅠㅠㅠㅠㅠㅠ 이런거 어떻게 알아야해 ㅠㅠㅠㅠ
    if flag2 == True:
        print(res_day-1)
'''
# 계속 틀렸던 이유
'''
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
'''