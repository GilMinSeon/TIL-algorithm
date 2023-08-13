n = int(input())

min_val = 1000000

for i in range(1,n):
    str_val = str(i)

    sum_val = 0
    for x in str_val:
        sum_val += int(x)

    if sum_val + i == n:
        if i < min_val:
            min_val = i

if min_val < 1000000:
    print(min_val)
else:
    print(0)

###########################################
# 다른 사람 풀이
n = int(input())
flag = False
for i in range(1, n):
    summ = sum(map(int, str(i)))
    if i + summ == n:
        print(i)
        flag = True
        break
if (flag == False):
    print('0')

###########################################
import sys
input = sys.stdin.readline

# 분해합: N
N = int(input())

# 가장 작은 생성자 구하기
for i in range(N):    
    # 각 자릿수 합
    num_sum = 0    
    
    # 각 자릿수를 구하고 합에 집어넣기
    j = i
    while True:
        if j < 10:
            num_sum += j % 10
            break
        else:
            num_sum += j % 10
            j = j // 10

    # 각 자릿수와 숫자 자체를 더해서 생성자가 맞는지 확인
    if N == i + num_sum:
        print(i)
        # 가장 작은 생성자 출력을 위해 i 값이 나오면 반복문 종료
        break
# 생성자가 없다면 0 출력
else:
    print(0)