import sys, heapq
input = sys.stdin.readline
a = []

n = int(input())
for i in range(n):
	num = int(input())
	if num:
		heapq.heappush(a, (abs(num), num))
	else:
		if a:
			print(heapq.heappop(a)[1])
		else:
			print(0)