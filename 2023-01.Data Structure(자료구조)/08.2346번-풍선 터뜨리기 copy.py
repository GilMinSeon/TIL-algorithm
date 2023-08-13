from collections import deque

n = int(input())
tmp = list(map(int, input().split()))
arr = []
for idx, val in enumerate(tmp):
    arr.append((idx+1, val))

cur = 0
res = []

for _ in range(n):
    i, j = arr.pop(cur)
    print(i, j, 'len(arr)===>', len(arr), '  cur===>', cur)
    # 종이에 0은 적혀있지 않다
    # 종이에는 -N보다 크거나 같고, N보다 작거나 같은 정수가 하나 적혀있다.
    if j > 0:
        cur += (j-1) # 한개 pop했으니까
    else:
        cur += j

        if cur < 0:
            print(cur, 'ddddd')
            cur = len(arr) - 1 + cur + 1
    print('변한 cur:::::', cur)


'''
5
3 2 1 -3 -1

정답 : 1 4 5 3 2
'''

'''
4
2 2 2 2
    
정답: 1 3 2 4
출력: 1 4 3 2 
'''