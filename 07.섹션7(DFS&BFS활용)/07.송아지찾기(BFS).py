from collections import deque

MAX = 10000

n, m = map(int, input().split())

# 체크배열과 최종답배열 두개 만들기
ch = [0]*(MAX+1)
dis = [0]*(MAX+1)

# 값이 없을때까지 돌릴 큐 하나 만들어서 거기다가 첫번째 값 넣어두기
dq = deque()
dq.append(n)

# 넣어둔 첫번째 값 체크
ch[n] = 1
dis[n] = 0  # 첫번째 값은 0번만에 갈수있음, 이제 다음 가지부터 dis[next] = dis[now] + 1 이렇게 해서 2,3,4,,, 레벨

while dq:
    # 일단 큐 맨 앞에서 하나 빼기!!!
    now = dq.popleft()

    # next 만들기 전에 체크!
    if now == m:
        print(dis[now])
        break
   
    for next in (now-1, now+1, now+5):
        # 좌표안에서만 돌아야함!
        if 0 < next <= MAX:
            # 여기서 한 번 더 체크, 방문한 곳인지 아닌지!
            if ch[next] == 0:
                dq.append(next) # 1) 큐에 넣어주고

                ch[next] = 1 # 2) 체크배열 값 체크해주고
                dis[next] = dis[now] + 1    # 3) dis에 지금 몇 레벨인지 값 써넣어주기!
