def DFS(L):
    global cnt
    print(str(L) + 'fffff')
    if L == m:
        for j in range(L):
            print(res[j], end = ' ')
        print('ddd')
        cnt += 1

    else:
        for i in range(1, n+1): ### 범위도 틀림 => 1 ~ n+1
            print('=====' + str(i) + '=======' + str(L))

            if ch[i] == 0:
                # 가지뻗을때
                ch[i] = 1
                res[L] = i

                DFS(L+1)
                # 여기는 back할때!!
                ch[i] = 0
            else:
                print('else' + str(i))
            


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0]*n
    ch = [0]*(n+1)
    cnt = 0
    DFS(0)
    print(cnt)

'''
내가 그냥 써보니까 다시 못 품
일단 res, ch 두가지 사용하는거 다시 공부하기
n과 m이 의미하는 것

'''