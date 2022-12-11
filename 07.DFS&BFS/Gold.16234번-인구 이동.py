from collections import deque
import sys

n, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n*n):
    board[i]