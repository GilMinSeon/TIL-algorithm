# pop 수행하면 시간복잡도 O(n)가 되어서 시간초과 오류 발생함!
# => front_idx를 활용하여 실제로 pop을 하지는 않으면서 큐 구현 가능~~!

import sys

n = int(sys.stdin.readline())
que = []
front_idx = 0

for _ in range(n):
    x = sys.stdin.readline().split()
    order = x[0]
    
    if order == 'push':
        que.append(int(x[1]))
        
    if order == 'pop':
        if front_idx == len(que): # 아니면 len(que) - front_idx == 0 도 가능
            print('-1')
        else:
            val = que[front_idx]
            print(val)
            #한 줄로 print(que[front_idx])
            front_idx += 1
            
    if order == 'size':
        print(len(que)-front_idx) # !! 중요 !!
        
    if order == 'empty':
        if front_idx == len(que):
            print('1')
        else:
            print('0')
            
    if order == 'front':
        if front_idx == len(que):
            print('-1')
        else:
            print(que[front_idx])
            
    if order == 'back':
        if front_idx == len(que):
            print('-1')
        else:
            print(que[-1])
