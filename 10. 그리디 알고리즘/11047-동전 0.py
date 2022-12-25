import sys
input = sys.stdin.readline

n, k = map(int, input().split())
money = []
for _ in range(n):
    money.append(int(input()))

money.reverse() # 그리디 알고리즘 - 정렬!

cnt = 0
while k!=0:
    # for i in range(n-1, 0, -1):
    #     if money[i] > k:
    #         continue
    #     else:
    #         tmp_cnt = (k // money[i])
    #         cnt += tmp_cnt
    #         k -= (money[i]*tmp_cnt)
    '''
    for i in range(n):
        if money[i] > k:
            continue
        else:
            tmp_cnt = (k // money[i])
            cnt += tmp_cnt
            k -= (money[i]*tmp_cnt)    
    '''
    for x in money:
        if x > k: continue
        cnt += k//x
        k = k%x

print(cnt)

'''
n, k = map(int, input().split())
li = []
cnt = 0
for i in range(n):
    li.append(int(input()))
li.sort(reverse=True)
for i in li:
    cnt += k//i
    k = k % i
print(cnt)
'''