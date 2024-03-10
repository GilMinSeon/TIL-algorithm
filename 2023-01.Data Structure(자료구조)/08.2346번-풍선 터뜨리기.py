from collections import deque

n = int(input())
tmp = list(map(int, input().split()))
arr = []
for idx, val in enumerate(tmp):
    arr.append((idx+1, val))

cur = 0
res = []

for case in range(n):
    i, j = arr.pop(cur)

    res.append(i)

    if len(arr) == 0:
        break
    
    # j값으로 분기하는게 아니라 현재 cur에서 j만큼 갔을때의 "값"과 len(arr) 비교해서 분기
    print('j===>', j, 'len===>', len(arr), 'cur===>', cur)
    if cur + j > len(arr):
        # 오른쪽으로 인덱스 넘는 경우
        print('case 1')
        cur = cur % len(arr)

    elif cur + j < 0:
        # 왼쪽으로 인덱스 넘는 경우 -> 이 경우에 무조건 양수 인덱스로 바꿔줘야함!
        print('case 2')


    elif cur + j == 0:
        pass
        print('case4')

    else:
        print('case3')
        cur += (j-1)


    print('변한 cur:::::', cur)
    print(res)


print(*res)



'''
5
3 2 1 -3 -1

정답 : 1 4 5 3 2
'''


'''
4
2 2 2 2
    
정답: 1 3 2 4
'''

'''
5
-5 -5 -5 -5 -5

정답: 1 5 3 2 4
'''