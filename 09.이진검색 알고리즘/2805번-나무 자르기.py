import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))

left = 1
right = max(tree)

# 절단기 높이로 설정될 len를 받았을때 잘린 나무의 합 리턴
def calc_height(len):
    sum = 0
    for x in tree:
        if x > len:
            sum += (x-len)
    return sum

res = 0 # 절단기에 설정할 높이의 최댓값

while left <= right:
    mid = (left + right) // 2

    if calc_height(mid) >= m:
        res = mid
        left = mid + 1
    else:
        right = mid - 1

print(res)
