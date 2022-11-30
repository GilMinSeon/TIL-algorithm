# BFS풀이
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]

# BFS를 하며 각 좌표를 몇번만에 가는지 갱신
dis = [[0]*m for _ in range(n)]

# BFS할 큐 배열 준비
dq = deque()

# BFS 함수
def BFS():
    while dq:
        now = dq.popleft()

        for i in range(4):
            a = now[0] + dx[i]
            b = now[1] + dy[i]

            # 1 : 이동할 수 있는 칸, 0 : 이동할 수 없는 칸
            if 0<=a<n and 0<=b<m and board[a][b] == 1:
                dq.append((a,b))
                board[a][b] = 0
                dis[a][b] = dis[now[0]][now[1]] + 1

# BFS 호출
dq.append((0,0))
dis[0][0] = 1
BFS()
print(dis[n-1][m-1])

