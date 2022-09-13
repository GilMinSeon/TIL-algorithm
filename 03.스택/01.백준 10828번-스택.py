import sys

input=sys.stdin.readline()

n = int(input)
stk = []
for _ in range(n):
    a = sys.stdin.readline().strip()
    if a[:4] == 'push':
        num = a[5:]
        stk.append(num)
    elif a == 'pop':
        if len(stk) == 0:
            print('-1')
        else:
            popVal = stk.pop()
            print(popVal)
    elif a == 'size':
        print(len(stk))
    elif a == 'empty':
        if len(stk) == 0:
            print('1')
        else:
            print('0')
    elif a == 'top':
        if len(stk) == 0:
            print('-1')
        else:
            print(stk[-1])
    
        
