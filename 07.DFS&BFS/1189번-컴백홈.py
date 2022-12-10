r, c, k = map(int, input().split())
board = [[0]*(c) for _ in range(r)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#board = [list(input().strip()[:]) for _ in range(r) ]
for i in range(r):
    tmp = input()
    for j in range(c):
        if tmp[j] == 'T':
            board[i][j] = 1

cnt = 1
res = 0

def DFS(x,y):
    global cnt
    global res
    #print(x,y)
    if (x,y) == (0, c-1):   # end지점
        #print(cnt)
        if cnt == k:
            res += 1
    else:
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if 0<=a<r and 0<=b<c and board[a][b] == 0:
                cnt += 1
                board[a][b] = 1
                DFS(a, b)
                cnt -= 1
                board[a][b] = 0

board[r-1][0] = 1
DFS(r-1, 0) # start지점
print(res)
