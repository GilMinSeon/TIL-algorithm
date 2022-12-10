# BFS풀이
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

h_set = set()

for i in range(n):
    for j in range(n):
        h_set.add(board[i][j])

# 더 빠르게 할 수 있는 방법 있는지 확인
#print(h_set)

# BFS할 큐 배열 준비
dq = deque()

# BFS 함수
def BFS(h):
    while dq:
        now = dq.popleft()

        for i in range(4):
            a = now[0] + dx[i]
            b = now[1] + dy[i]

            if 0<=a<n and 0<=b<n and board[a][b] > h and ch[a][b] == 0:
                dq.append((a,b))
                ch[a][b] = 1


res = [1]
for _ in range(len(h_set)):
    h = h_set.pop()
    ch = [[0]*n for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(n):
            
            if board[i][j] > h and ch[i][j] == 0:
                dq.append((i,j))
                ch[i][j] = 1
                BFS(h)
                cnt += 1

    res.append(cnt)

print(max(res))

