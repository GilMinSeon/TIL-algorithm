# 인프런 page7. 가장 높은 탑 쌓기
n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
print(arr)
arr.sort(key=lambda x:x[0], reverse=True)
print(arr)