
from collections import deque

F, S, G, U, D = map(int, input().split())
# 총 F층, 현재 S층, G층 가고싶음, U만큼 위로, D만큼 아래로

Q = deque()

dis = [0]*(F+1)
visited = [0]*(F+1)

visited[S] = 1

Q.append(S)

while True:
    if S == G:
        print('0')
        break

    if dis[G] != 0:
        print(dis[G])
        break

    if len(Q) == 0:
        print('use the stairs')
        break
    
    now = Q.popleft()

    for next in (now+U, now-D):
        if 0<next<=F and visited[next] == 0:
            visited[next] = 1
            Q.append(next)
            dis[next] = dis[now] + 1

    



'''
#[0, 0, 2, 1, 3, 2, 4, 3, 5, 4, 6]
import sys
from collections import deque

def bfs(v):
    q = deque([v])
    visited[v] = 1
    while q:
        v = q.popleft()
        if v == G:
            return count[G]
        for i in (v+U, v-D): #U만큼 위로 or D만큼 아래로
            if 0 < i <= F and not visited[i]:
                visited[i] = 1
                count[i] = count[v] + 1
                q.append(i)
    if count[G] == 0:
        return "use the stairs"

input = sys.stdin.readline
F, S, G, U, D = map(int, input().split())
visited = [0 for i in range(F+1)]
count = [0 for i in range(F+1)]
print(bfs(S))
print(count)

'''