'''
0 0 0 0 0 0 0 
0 1 1 1 1 1 0 
0 0 0 1 0 0 0 
1 1 0 1 0 1 1 
1 1 0 0 0 0 1 
1 1 0 1 1 0 0 
1 0 0 0 0 0 0 
'''
n = 7
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

board = [list(map(int, input().split())) for _ in range(n)]

board[0][0] = 1 #############이거 한 줄!!!!!!!!때문에 계속 16 나옴

cnt = 0

def DFS(x,y):
    global cnt
    if (x,y) == (6,6):
        cnt += 1

    else:
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if 0<=a<n and 0<=b<n:
                if board[a][b] == 0:
                    board[a][b] = 1
                    DFS(a, b)
                    board[a][b] = 0

DFS(0,0)
print(cnt)