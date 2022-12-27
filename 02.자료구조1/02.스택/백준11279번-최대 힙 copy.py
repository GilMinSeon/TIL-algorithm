import heapq as hq
import sys
input = sys.stdin.readline
n = int(input())
a = []
for _ in range(n):
    x = int(input())
    if x == 0:
        if len(a) == 0:
            print('0')
        else:
            print(-hq.heappop(a)) # 음수화
    else:
        hq.heappush(a, -x) # 음수화

