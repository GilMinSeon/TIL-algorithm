'''
한 번에 통과했다!!!
'''

import sys
input=sys.stdin.readline()

n = int(input)

for _ in range(n):
    stk = []
    a = sys.stdin.readline().strip()
    
    for i in a:
        pass
        # 왼쪽 괄호인지 오른쪽 괄호인지 분기
        if i == '(':
            stk.append(i)
        else:
            if len(stk) == 0:
                print('NO')
                break
            else:
                stk.pop()
    else:
        if len(stk) > 0:
            print('NO')
        else:
            print('YES')
