'''
9 : target
-1 0 3 5 9 12 : nums
'''

target = int(input())
nums = list(map(int, input().split()))

left = 0
right = len(nums) - 1

while left <= right:
    mid = (left + right) // 2

    if nums[mid] == target:
        print(mid)
        break
    elif nums[mid] > target:
        right = mid - 1
    else:
        left = mid + 1

# 찾지 못하는 경우도 있다면
#print(-1)