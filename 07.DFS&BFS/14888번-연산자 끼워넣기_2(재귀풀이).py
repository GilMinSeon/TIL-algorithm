# https://www.youtube.com/watch?v=I5G2uU8GGZg
n = int(input())
arr = list(map(int, input().split()))
operator = list(map(int, input().split()))
min_val, max_val = 100000000, -100000000

# 연산자 배치 함수
def DFS(L, calc_val):
    global min_val, max_val
    if L == n-1:
        min_val = min(calc_val, min_val)
        max_val = max(calc_val, max_val)
    else:
        for i in range(4):
            if operator[i] != 0:
                operator[i] -= 1
                # DFS() 호출 => 호출하면서 해줘야 하는일 1. 레벨 증가 2. calc_val 셋팅
                DFS(L+1, calc(L, i, calc_val))
                operator[i] += 1

# 연산자 셋팅되면 계산해주는 함수
def calc(L, op, val):
    a = arr[0] if L == 0 else val
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

DFS(0, 0)
print(max_val)
print(min_val)