# 시간초과에 안 걸림
# index를 이용하는게 아니라 pop을 수행 -> 시간 오래걸림 => 보완한게 큐2 문제

import sys

n = int(sys.stdin.readline())
que = []

for _ in range(n):
    x = sys.stdin.readline().split()
    order = x[0]
    if order == 'push':
        que.append(int(x[1]))
    if order == 'pop':
        if not que: # 비어있으면 False니까 not 붙여서 True로 만든다!!!!!!!!!!!
            print('-1')
        else:
            print(que[0])
            que.pop(0)
    if order == 'size':
        print(len(que))
    if order == 'empty':
        if not que:
            print('1')
        else:
            print('0')
    if order == 'front':
        if not que:
            print('-1')
        else:
            print(que[0])
    if order == 'back':
        if not que:
            print('-1')
        else:
            print(que[-1])
