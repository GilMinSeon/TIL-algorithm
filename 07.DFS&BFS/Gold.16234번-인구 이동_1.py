from collections import deque
import sys

N, L, R = map(int, input().split()) #인구 차이가 L명 이상, R명 이하
board = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def BFS(xx, yy, idx):
    dq = deque([])
    dq.append([xx, yy])
    cnt = 1
    sum = board[xx][yy]
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<N and 0<=ny<N and bfs_board[nx][ny] == 0:
                org, new = board[x][y], board[nx][ny]
                if L<=abs(org-new)<=R:
                    dq.append([nx, ny])
                    bfs_board[nx][ny] = idx
                    cnt += 1
                    sum += board[nx][ny]
    return cnt, sum

res = 0
ch = []
ch_board = [[0]*N for _ in range(N)]
while True:
    tmp = []
    bfs_board = [[0]*N for _ in range(N)]
    area_idx = 1
    for i in range(N):
        for j in range(N):
            if bfs_board[i][j] == 0 and ch_board[i][j] != True:
                bfs_board[i][j] = area_idx
                cnt, sum = BFS(i, j, area_idx)
                # 하고나서 bfs 끝났을때 인구이동 하기
                tmp.append([cnt, sum, area_idx])
                area_idx += 1
    flag = True
    ch = []
    ch_board = [[0]*N for _ in range(N)]
    union_cnt = 0
    for x, y, z in tmp:
        if x > 1:
            flag = False
            union_cnt += 1
            div = y // x
            for i in range(N):
                for j in range(N):
                    if bfs_board[i][j] == z:
                        ch.append([i, j])
                        board[i][j] = div
                        ch_board[i][j] = True

    if union_cnt != 1:
        ch = []

    if flag:
        break
    else:
        res += 1

    # for i in range(N):
    #     print(bfs_board[i])

    # print()
    # print()
    
print(res)


'''
Phase 마다 BFS 로 각 노드마다 탐색을 하면서 이미 이번 Phase 에서 방문한 노드는 건너띄는 전략을 취한다는 가정 하에서
한번 연합 A 가 만들어지면 평균치로 조정되고, 다른 국가랑 합쳐지지 않는 한 변하지 않습니다.
A 가 한번 합쳐지고 다음 페이즈에는 그대로라고 합시다.
이때 인근 외부의 연합 B 가 생겨서 수가 조정되면 다시 연합할 여지가 생깁니다.
그러면 외부 인근 국가 B 에서 BFS 로 해서 A 까지 탐색하면 이는 연합이 되는거고 그렇지 않으면 연합이 되지 않습니다.
*****즉 연합 A 는 탐색할 필요가 없고 외부에서 새로 연합된 것들만 탐색하면 되는 겁니다.*****
이를 체크하면 빨라진다는 것이 요지입니다.
'''

'''
import sys
from collections import deque

N, L, R = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def grouping(r, c, num):
    Q = deque([(r, c)])
    groups[r][c] = num
    total = arr[r][c]
    cnt = 1
    while Q:
        r, c = Q.popleft()
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < N and 0 <= nc < N and L <= abs(arr[nr][nc] - arr[r][c]) <= R and groups[nr][nc] < groups[r][c]:
                groups[nr][nc] = num
                Q.append((nr, nc))
                total += arr[nr][nc]
                cnt += 1
    return total // cnt


flag = True
days = 0
changes = []
groups = [[0] * N for _ in range(N)]
populations = [0]
group_num = 0
while flag:
    flag = False

    if changes:
        for change in changes:
            r, c = change
            group_num += 1
            populations.append(grouping(r, c, group_num))
    else:
        for r in range(N):
            for c in range(N):
                if not groups[r][c]:
                    group_num += 1
                    populations.append(grouping(r, c, group_num))
    tmp = []
    for r in range(N):
        for c in range(N):
            if arr[r][c] != populations[groups[r][c]]:
                tmp.append((r, c))
                arr[r][c] = populations[groups[r][c]]

    if tmp:
        changes = tmp
        flag = True
        days += 1

print(days)
'''

# 파이썬 느리지만 통과 => 일단 이것부터 분석하기!!!
'''
from collections import deque
import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    union = []
    union.append((x, y))
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            n_x = x + dx
            n_y = y + dy
            if 0 <= n_x < N and 0 <= n_y < N and not visited[n_x][n_y]:
                if L <= abs(graph[x][y] - graph[n_x][n_y]) <= R:
                    q.append((n_x, n_y))
                    union.append((n_x, n_y))
                    visited[n_x][n_y] = True
    return union


count = 0
while True:
    is_move = False
    visited = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                union = bfs(i, j)
                if len(union) > 1:
                    is_move = True
                    avg_population = sum([graph[x][y] for x, y in union]) // len(union)
                    for x, y in union:
                        graph[x][y] = avg_population

    if not is_move:
        break
    count += 1

print(count)


'''