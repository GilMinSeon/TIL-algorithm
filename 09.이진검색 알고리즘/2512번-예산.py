import sys
input = sys.stdin.readline

n = int(input())
budget = list(map(int, input().split()))
m = int(input())

left = 1
right = max(budget)

def calc(val):
    sum = 0
    for x in budget:
        if x <= val:
            sum += x
        else:
            sum += val
    return sum

res = 0

while left <= right:
    mid = (left + right) // 2

    if calc(mid) <= m: # m이라는 예산을 넘어서는 안된다
        res = mid
        left = mid + 1
    else:
        right = mid - 1

print(res)
