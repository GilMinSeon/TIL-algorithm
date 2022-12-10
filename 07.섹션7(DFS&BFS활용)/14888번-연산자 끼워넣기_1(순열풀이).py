n = int(input())
arr = list(map(int, input().split()))
temp = map(int, input().split())
operator = []

for idx, val in enumerate(temp):
    if val == 0:
        continue
    if val > 1:
        for _ in range(val):
            operator.append(idx)
    else:
        operator.append(idx)

#print(operator)

min_val = 100000000
max_val = -100000000

# 연산자 순서 배치하는 순열 함수
def DFS(L, calc_val):
    global min_val
    global max_val

    if L == n-1:
        #print(res, '     ', calc_val)
        min_val = min(calc_val, min_val)
        max_val = max(calc_val, max_val)
    else:
        for i in range(n-1):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = operator[i]
                #print('calc:::::::', calc(L, operator[i], calc_val))
                DFS(L+1, calc(L, operator[i], calc_val))
                ch[i] = 0

# 연산자 셋팅되면 계산해주는 함수
def calc(L, op, val):
    a = arr[L] if L == 0 else val
    b = arr[L+1]
    if op == 0:
        return a+b
    elif op == 1:
        return a-b
    elif op == 2:
        return a*b
    else:
        if a<0 or b<0:
            return (abs(a)//abs(b))*-1
        else:
            return a//b
res = [0]*(n-1)
ch = [0]*n
DFS(0, 0)
print(max_val)
print(min_val)