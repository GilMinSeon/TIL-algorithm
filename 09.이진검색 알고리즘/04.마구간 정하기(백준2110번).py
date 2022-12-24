# 결정알고리즘
# 4번. 마구간 정하기 => 일단 강사님 문제해설 듣고 내가 코드 짬!

n, c = map(int, input().split()) #n개의 마구간, c마리의 말
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()

left = 1    # min(arr) => min값이 아님!!!!
'''
lt부터 rt값의 범위는 마구간의 좌표를 의미하는 것이 아니라 
이 문제의 답인 가장 가까운 두 말의 최대 거리값 즉 이 문제의 답이 확실하게 존해한다는 범위를 지정한 것입니다. 
만약 아래 입력의 경우
5 3
5
6
12
8
14
의 경우 답이 3인데  lt=line[0]으로 초기화 하면 답을 5 ~ 14 사이에서 찾게 됩니다.
'''
right = max(arr)

def fn_calc(dis):
    standard = arr[0]
    cnt = 1
    for i in range(1, n):
        if arr[i] - standard >= dis:
            cnt += 1
            standard = arr[i]
    return cnt

res = 0
while left <= right:
    mid = (left + right) // 2
    calc_val = fn_calc(mid)# 두말의 최대거리를 던져서 c마리의 말을 놓을 수 있는가 확인
    # 만약 calc_val이 문제가 요구하는 c마리보다 적게! 리턴한다면 
    # 너무 거리가 멀다는 뜻 -> so, right를 줄여서 거리를 작게 만들기
    # else: c마리를 리턴하거나 그 이상을 리턴한다면 가능하다는 얘기니까 left를 증가시켜서 최적의 답 찾기

    if calc_val >= c:
        res = mid
        left = mid + 1
    else:
        right = mid - 1

print(res)
