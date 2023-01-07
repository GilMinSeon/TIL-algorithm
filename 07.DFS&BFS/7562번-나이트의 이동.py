import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

'''
각 테스트 케이스는 세 줄로 이루어져 있다. 
첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다.
체스판의 크기는 l × l이다. 
체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다. 
둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.

각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력한다. -> 최소니까 BFS
'''

# 방향 설정
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

for _ in range(T):
    n = int(input())
    nx, ny = map(int, input().split()) # now 현재 지점
    tx, ty = map(int, input().split()) # target 지점

    board = [[0]*(n) for _ in range(n)]
    dq = deque([])
    dq.append([nx, ny])
    board[nx][ny] = 1 # visited
    
    while dq:
        x, y = dq.popleft()

        if (x,y) == (tx,ty):
            print(board[x][y]-1)
            break

        for i in range(8):
            a = dx[i] + x
            b = dy[i] + y

            if 0<=a<n and 0<=b<n and board[a][b] == 0:
                board[a][b] = board[x][y] + 1
                dq.append([a,b])
        
        
    