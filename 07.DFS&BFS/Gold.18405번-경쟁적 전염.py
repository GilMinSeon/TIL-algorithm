from collections import deque
import sys

n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dq = deque()
data = []
for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            data.append([board[i][j], i, j])
data.sort()
#dq = deque([data]) # ===> 이건 오답! popleft할때 전부 꺼내짐
dq = deque(data)    # 바로 deque화 하면 됨, 한 번더 리스트화 할 필요 없음
def BFS():
    global second
    while dq:
        if second == s: break
        for _ in range(len(dq)):
            virus, x, y = dq.popleft() # x y -> 0 0
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0<=nx<n and 0<=ny<n and board[nx][ny] == 0:
                    board[nx][ny] = virus
                    dq.append([virus, nx, ny])
        second += 1

second = 0
BFS()
print(board[x-1][y-1])


'''
q.append(data)와 q=deque(data)는 차이가 있다.
우선 data는 리스트다. [(),(),()] 형태이다.
q=deque를 하면 deque([])가 생긴.
q.append(data)같은경우 위에서 deque()을 만들어 주고, 
그안에 data를 리스트를 씌워서 더하는 방식이다. 그러면 ([[(),(),()]]) 형태가 된다.

q=deque(data)의 경우에는 deque선언괴 동시에 그 안에 data를 넣기 때문에 
deque([(),(),()])형태가 된다.
'''
