n,m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

hs = []
ch = []
cb = [0]*m
res = 2147000000

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            hs.append((i,j))
        elif board[i][j] == 2:
            ch.append((i,j))

def DFS(L, s):
    global res
    if L == m:
        sum = 0
        for j in range(len(hs)):
            x1 = hs[j][0]
            y1 = hs[j][1]
            dis = 2147000000
            for x in cb:
                x2 = ch[x][0]
                y2 = ch[x][1]
                dis = min(dis, abs(x1-x2) + abs(y1-y2))
            sum += dis

        if sum<res:
            res = sum

    else:
        for i in range(s, len(ch)):
            cb[L] = i
            DFS(L+1, i+1)

DFS(0,0)
print(res)


'''
from collections import deque

def distance(chicken):  # 거리를 계산하는 함수
    dist = 0
    for r1, c1 in home:
        dist += min([(abs(r1 - r2) + abs(c1 - c2)) for r2, c2 in chicken])
    return dist


def dfs(n, index):  # 조합을 만들어 치킨 거리의 최솟값을 찾는 함수 # n: 고른 치킨집 수 i: 고른 치킨집 번호
    global min_dist

    # 모든 치킨집을 골랐다면 치킨거리 계산
    if n == M:
        select_chicken = [chicken[i] for i in range(chickenCount) if visited[i]]
        min_dist = min(min_dist, distance(select_chicken))
        return

    # DFS 사용하여 조합 구하기
    for i in range(index, chickenCount):
        if visited[i] == 0:
            visited[i] = 1
            dfs(n + 1, i + 1)
            visited[i] = 0


if __name__ == "__main__":

    N, M = map(int, input().split())  # 도시 크기, 치킨집 개수
    city = deque([])  # 도시
    chicken = deque([])  # 치킨집
    home = deque([])  # 집

    for r in range(N):
        temp = list(map(int, input().split()))
        city.append(temp)  # 도시의 각 행에 대한 정보 추가
        for c in range(N):
            if temp[c] == 2:  # 치킨집인 경우
                chicken.append((r, c))
            elif temp[c] == 1:  # 집인 경우
                home.append((r, c))

    if len(chicken) == M:  # 이미 M개이므로 치킨집을 폐업시킬 필요가 없음
        print(distance(chicken))
    else:  # M개씩 조합을 만들어 도시의 치킨 거리의 최솟값을 찾아야 함
        min_dist = N * 2 * len(home)  # 총 치킨거리 임의의 큰 값
        chickenCount = len(chicken)
        visited = [0] * chickenCount
        dfs(0, 0)
        print(min_dist)
'''