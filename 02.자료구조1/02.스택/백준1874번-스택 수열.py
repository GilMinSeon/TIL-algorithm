import sys
input = sys.stdin.readline

n = int(input())

stk = []
cnt = 0  
msg = ''
for _ in range(n):
    target = int(input())

    while cnt < target:
        cnt += 1
        stk.append(cnt)
        msg += '+'

    if stk[-1] == target:
        stk.pop()
        msg += '-'
    else:
        print('NO')
        sys.exit(0)

for x in msg:
    print(x, end='\n')
