def factorize2(n):
    factor = 2
    factors = []

    while factor**2 <= n:
        while n % factor == 0:
            n //= factor
            factors.append(factor)
        
        factor += 1
    
    if n > 1:
        factors.append(n)
    
    return factors


#print(factorize2(17))

# 간단한 방법
def factorization(x):
    d = 2
    while d <= x:   # 이 코드는 d**2 해주면 안됨, 왜냐면 5나 17인 경우 자기자신까지 돌아야 출력가능 so, 거듭제곱으로 주면 안됨! 즉 d+=1해서 d가 5가 되고나서 d가 6될때 while문 탈출
        if x % d == 0: 
            print(d)
            x //= d
        else:
            d += 1

factorization(5)
