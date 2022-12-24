import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

card.sort()

for i in range(m):
    target = nums[i]

    left = 0
    right = n-1
    flag = True
    while left <= right:
        mid = (left + right) // 2
        if card[mid] == target:
            print('1')
            flag = False
            break
        elif card[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    if flag : print('0')

###########다른 사람 풀이 - 깔끔########### => 함수 부르는게 나을듯, flag 변수 사용 안해도 됨
N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
X = list(map(int, input().split()))

def binary_search(nums, n):
  start = 0
  end = N-1
  while start<=end:
    mid = (start+end)//2
    if nums[mid]==n:
      return 1
    elif nums[mid]>n:
      end = mid-1
    elif nums[mid]<n:
      start = mid+1

  return 0

for x in X:
  print(binary_search(A, x))