from collections import deque

n = int(input())
arr = deque([i for i in range(1, n+1)])

while len(arr) != 1:
    arr.popleft()
    arr.append(arr.popleft())

print(*arr)

'''
import sys
from collections import deque

n = int(sys.stdin.readline())
dq = deque([x for x in range(1, n+1)])


while True:
    # input이 1일때 런타임에러! if문 위치를 pop위로 올려야함
    if len(dq) == 1:
        print(dq[0])
        break

    dq.popleft()
    dq.append(dq.popleft())
'''
