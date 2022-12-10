import sys
from collections import deque

def DFS(idx):
    # idx 1부터 시작 s의 검사가 모두 끝나면 수열의 가장 큰 값을 찾는다.
    if idx == len(s):
        print(*list(map(int,(result))))
        sys.exit()
    
    # dfs로 배열에 하나넣거나 두개는경우를 동시에 둘 다 조사하며 재귀 진행.(분기가 있는 DFS)
    # 글자 하나만 조사.idx 하나 건너뛴다.
    if int(s[idx]) <= n and visited[int(s[idx])] == 0:
        #print('1_1 ====>',s[idx])
        visited[int(s[idx])] = 1
        result.append(s[idx])
        DFS(idx+1)
        #print('1_2 ====>',s[idx])
        result.pop()
        visited[int(s[idx])] = 0

    # 글자 두개조사. 두개짤랐을때 n이하. 그리고 그 숫자가 전에 방문한적 없었을때 방문.idx 2개 건너뛴다.
    if int(s[idx:idx+2]) <= n and visited[int(s[idx:idx+2])] == 0:
        #print('2_1 ====>',s[idx:idx+2])
        visited[int(s[idx:idx+2])] = 1
        result.append(s[idx:idx+2])
        DFS(idx+2)
        #print('2_2 ====>',s[idx:idx+2])
        visited[int(s[idx:idx+2])] = 0
        result.pop()

s = input()
n = 0
if len(s) <= 9:
    n = len(s)
else:
    n = (len(s) - 9)//2 + 9

result = deque()
visited = [0] * (n+1)
visited[0] = 1
DFS(0)

#155987643211011121314
#15 5 9 8 7 6 4 3 2 1 10 11 12 13 14