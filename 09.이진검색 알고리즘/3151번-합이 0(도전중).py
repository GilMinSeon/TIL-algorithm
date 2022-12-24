import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

#[-6, -5, -4, -4, 0, 1, 2, 2, 3, 7]

res = 0

for i in range(n-1):
    start = arr[i]
    print(start)

    left = i+1
    right = n-1

    while left <= right:
        mid = (left + right) // 2
        calc = start + arr[left] + arr[right]

        if calc == 0:
            res += 1
            print(start, arr[left], arr[right])
            break
        elif calc > 0:
            right = mid - 1
        else:
            left = mid + 1