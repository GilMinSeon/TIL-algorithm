# 문자열, 브루트포스 알고리즘

import sys
input = sys.stdin.readline

a, b = input().split()

cnt = 0
if len(a) == len(b):
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
    print(cnt)

else:
    if a in b:
        print(0)
    else:
        min_res =len(a)#최댓값으로 가정
        for i in range(len(b)-len(a)+1):#B의 시작점 지정
            result=0
            #A와 문자열 비교
            for j in range(len(a)):
                if a[j]!=b[i+j]:
                    result+=1
                #최솟값이 앞에 구한것보다 커지면 그만두기(시간을 줄이기 위해 추가)
                if result>min_res:
                    break
            #앞에서 구한 최솟값과 현재 구한 최솟값 비교
            min_res=min(min_res,result)
        
        print(min_res)
