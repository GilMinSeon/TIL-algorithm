import sys
input = sys.stdin.readline

n = int(input())

stk = []
cur = 0 # 어디까지 넣었는지 기억
res = []
flag = True  

for _ in range(n):
    target = int(input())

    while cur < target:
        cur += 1
        stk.append(cur)
        res.append('+')

    #print(cur)

    if stk[-1] == target:
        stk.pop()
        res.append('-')
    else:
        flag = False
        break

if flag == False:
    print("NO")
else:
    for i in res:
        print(i)