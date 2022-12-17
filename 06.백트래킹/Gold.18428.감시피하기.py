import sys, copy
from collections import deque

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
board = [list(map(str, input().split())) for _ in range(n)]

t_set = set()

teacher = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 'T':
            teacher.append([i,j])
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0<=nx<n and 0<=ny<n and board[nx][ny] == 'X':
                    t_set.add((nx,ny))

t_list = list(t_set)

# 직선 방향 확인 함수
def check_S(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 직선 방향으로 확인
        while 0<= nx < n and 0<= ny < n and board[nx][ny] !='O':
            if board[nx][ny] == 'S':
                # 감시가능하다
                return True            
            else:        
                # T 나 X으면 계속 탐색
                nx += dx[i]
                ny += dy[i]
    # 감시 불가능하다
    return False

def DFS(L, s):
    if L == 3:
        cnt = 0
        for t in teacher:
            if not check_S(t[0], t[1]):
                cnt += 1

        if cnt == len(teacher):
            print('YES')
            sys.exit(0)
        
    else:
        for i in range(s, len(t_list)):
            board[t_list[i][0]][t_list[i][1]] = 'O'
            DFS(L+1, i+1)
            board[t_list[i][0]][t_list[i][1]] = 'X'
            
DFS(0,0)
print('NO')