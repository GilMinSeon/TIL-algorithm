import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort() #[1, 2, 3, 3, 4]

tot = 0
time = 0

for i in range(n):
    tot += arr[i]
    time += tot

print(time)