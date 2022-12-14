# 다른 사람 풀이 보고 인구이동 계산 하는 부분 최적화! => 평범한 BFS 풀이
'''
from collections import deque
import sys

N, L, R = map(int, input().split()) #인구 차이가 L명 이상, R명 이하
board = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(xx, yy):
    dq = deque([])
    dq.append([xx, yy])
    
    union = []
    union.append([xx,yy])

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0:
                org, new = board[x][y], board[nx][ny]
                if L<=abs(org-new)<=R:
                    dq.append([nx, ny])
                    union.append([nx, ny])
                    visited[nx][ny] = 1
    return union

res = 0
while True:
    visited = [[0]*N for _ in range(N)]
    flag = False

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                union = BFS(i, j)
                # 한번 끝났을때 인구이동 하기 -> 실제 board판 변경
                if len(union) > 1:
                    flag = True
                    ############ 이부분을 기억하기 start####################
                    avg = sum([board[x][y] for x, y in union]) // len(union)
                    for x, y in union:
                        board[x][y] = avg
                    ############ 이부분을 기억하기 start####################
    if not flag:
        print(res)
        break
    res += 1
'''
    
# 인구 이동
# 백준 16234
# https://www.acmicpc.net/problem/16234
# 14:25 - 
# avg 대입과정 최적화
# 찾는 범위를 벽돌쌓듯 진행

# 전날에 값을 변경한 근처만 조사할수있도록 변경

import sys
from collections import deque

input = sys.stdin.readline

N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
check = [[0]*N for _ in range(N)]
flag = False

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y, check, pos_tmp):
    global flag
    q = deque()
    q.append((x, y))
    
    cal_list = [(x, y)]
    sum = graph[x][y]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if check[nx][ny]:
                continue
            if L <= abs(graph[x][y] - graph[nx][ny]) <= R:
                q.append((nx, ny))
                cal_list.append((nx, ny))
                sum += graph[nx][ny]
                check[nx][ny] = 1
    
    if len(cal_list) > 1:
        flag = True
        avg = sum // len(cal_list)
        for x, y in cal_list:
            graph[x][y] = avg
            pos_tmp.append((x, y))

def solution():
    day = 0
    global flag

    #pos = [(x, y) for x in range(N) for y in range(x%2, N, 2)]
    pos = []
    print(pos)

    print('ddd')
    while True:
        flag = False
        pos_tmp = list()
        check = [[0]*N for _ in range(N)]
        print(pos)
        for x, y in pos:
            if not check[x][y]:
                check[x][y] = 1
                bfs(x, y, check, pos_tmp)
        if not flag:
            return day

        day += 1
        pos = pos_tmp
        
                    
if __name__ == "__main__":
    print(solution())