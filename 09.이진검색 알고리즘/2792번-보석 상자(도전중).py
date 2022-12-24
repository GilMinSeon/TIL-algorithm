import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 학생수, 보석종류

arr = []
for _ in range(m):
    arr.append(int(input()))

arr.sort()

left = 1
right = max(arr)

def calc(len):
    max_val = 0
    for x in arr:
        max_val = min(max_val, x if x==len else x//len + x%len)

while left <= right:
    mid = (left + right) // 2
    calc_val = calc(mid)
    if mid >= n:
        print(mid)
        right = mid - 1
    else:
        left = mid + 1
