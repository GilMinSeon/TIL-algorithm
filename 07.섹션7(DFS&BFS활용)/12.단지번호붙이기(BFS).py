'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
'''

# 반례!
'''
4
1000
0000
0000
0001
'''
# BFS풀이
from collections import deque

n = int(input())
board = [list(map(int, input())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# BFS할 큐 배열 준비
dq = deque()

# 정답 출력할 변수
res = []
cnt = 0

# BFS 함수
def BFS():
    global cnt

    while dq:
        cnt += 1
        now = dq.popleft()

        for i in range(4):
            a = now[0] + dx[i]
            b = now[1] + dy[i]

            if 0<=a<n and 0<=b<n and board[a][b]==1:
                dq.append((a,b))
                board[a][b] = 0


# BFS 호출
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            cnt = 0
            dq.append((i,j))
            board[i][j] = 0
            BFS()
            res.append(cnt)
            
# 출력
print(len(res))
res.sort()
for i in range(len(res)):
    print(res[i])

