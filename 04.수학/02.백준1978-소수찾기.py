'''
문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

출력
주어진 수들 중 소수의 개수를 출력한다.
'''
# 1) 내가 푼 방법 -> 68ms
n = int(input())
a = list(map(int, input().split()))
cnt = 0

def is_prime(x):
    for i in range(2, int(x ** 0.5)+1):
        if x % i == 0:
            return False
    return True

for x in a:
    if x == 1: continue
    if is_prime(x):
        cnt += 1
print(cnt)

# 2) 백준 다른 사람 풀이
'''
n=int(input())
li=list(map(int,input().split()))
cnt=0
for i in li:
    f=True
    if i<=1:continue
    for j in range(2,i):
        if i%j==0:
            f=False
            break
    if f:
        cnt+=1
print(cnt)

'''
    