'''
튜플 활용해서 푸는 문제!
그리고 계속 append 시키는 문제일 경우 for문 사용 불가 -> 계속 늘어나니까
while True/break 구조에 익숙해지기
'''
import sys
from collections import deque

num = int(sys.stdin.readline())

for _ in range(num):
    n, m = map(int, sys.stdin.readline().split())
    lst = list(map(int, sys.stdin.readline().split()))

    dq = [(idx, val) for idx, val in enumerate(lst)]
    dq = deque(dq)

    cnt = 0 # 몇번째
    while True:
        cur = dq.popleft()

        if any(cur[1] < x[1] for x in dq):
            dq.append(cur)
        else:
            cnt += 1
            if cur[0] == m:
                print(cnt)
                break
            
