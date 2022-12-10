# BFS풀이
from collections import deque

n, k = map(int, input().split())

# BFS를 하며 각 좌표를 몇번만에 가는지 갱신
dis = [0 for i in range(100001)]

# BFS할 큐 배열 준비
dq = deque()

# BFS 함수
def BFS():
    while dq:
        now = dq.popleft()

        if now == k:    # 종료조건
            break

        for next in (now-1, now+1, now*2):
            if 0 <= next <= 100000:
                if dis[next] == 0:
                    dq.append(next)
                    dis[next] = dis[now] + 1

# BFS 호출
dq.append(n)
BFS()
print(dis[k])



