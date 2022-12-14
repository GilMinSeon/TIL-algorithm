'''
Phase 마다 BFS 로 각 노드마다 탐색을 하면서 이미 이번 Phase 에서 방문한 노드는 건너띄는 전략을 취한다는 가정 하에서
한번 연합 A 가 만들어지면 평균치로 조정되고, 다른 국가랑 합쳐지지 않는 한 변하지 않습니다.
A 가 한번 합쳐지고 다음 페이즈에는 그대로라고 합시다.
이때 인근 외부의 연합 B 가 생겨서 수가 조정되면 다시 연합할 여지가 생깁니다.
그러면 외부 인근 국가 B 에서 BFS 로 해서 A 까지 탐색하면 이는 연합이 되는거고 그렇지 않으면 연합이 되지 않습니다.
*****즉 연합 A 는 탐색할 필요가 없고 외부에서 새로 연합된 것들만 탐색하면 되는 겁니다.*****
이를 체크하면 빨라진다는 것이 요지입니다.
'''

# 파이썬 느리지만 통과 => 일단 이것부터 분석하기!!!

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
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if L <= abs(graph[x][y] - graph[nx][ny]) <= R:
                    q.append((nx, ny))
                    union.append((nx, ny))
                    visited[nx][ny] = True
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
