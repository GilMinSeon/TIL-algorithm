# 결정알고리즘
k, n = map(int, input().split())
line = []

for _ in range(k):
    line.append(int(input()))

left = 1
right = max(line)

def fn_count(len):
    cnt = 0
    for x in line:
        cnt += (x//len)
    return cnt

res = 0 # 랜선의 길이

while left <= right:
    mid = (left + right) // 2

    if fn_count(mid) >= n:
        res = mid
        left = mid + 1
    else:
        right = mid - 1

print(res)
