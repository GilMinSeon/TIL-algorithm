# Gold 백트래킹, 1987번-알파벳
from collections import deque

R, C = map(int, input().split())
board=[list(input()) for _ in range(R)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y, cnt):
    global res
    res = max(res, cnt)

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0<=nx<R and 0<=ny<C:
            if ch_alpha[ord(board[nx][ny])-65]:
                ch_alpha[ord(board[nx][ny])-65] = False
                DFS(nx, ny, cnt + 1)
                ch_alpha[ord(board[nx][ny])-65] = True


ch_alpha = [True]*26

res = -2147000000
ch_alpha[ord(board[0][0])-65] = False
DFS(0, 0, 1)

print(res)

'''
set을 만들어서 이전 알파벳이 나왔는지 확인하는 방법이 느려서 시간 초과가 나는 듯하네요.
알파벳에 해당하는 길이 26의 배열을 만들어서 true, false 이런 식으로 관리해주면 빠를 겁니다.
'''
# 일단 visited 배열은 필요없엇다!!! 잘 생각하기!!!