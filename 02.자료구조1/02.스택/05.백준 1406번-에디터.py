'''
한번에 품
40분걸림
다른사람 간단하게 푼 풀이 볼것
print하는 코드 정리할것
'''

import sys
from collections import deque

input = sys.stdin.readline

s = input().rstrip()
n = len(s)
m = int(input())

stk = list(s)
dq = deque()

for _ in range(m):
    order = input().split()

    if order[0] == 'L':
        if stk:
            dq.append(stk.pop())
    
    elif order[0] == 'D':
        if dq:
            stk.append(dq.pop())
    
    elif order[0] == 'B':
        if stk:
            stk.pop()
    
    elif order[0] == 'P':
        stk.append(order[1])


res = ''.join(map(str, stk))

for _ in range(len(dq)):
    #print(dq.pop())
    res += dq.pop()

print(res)

