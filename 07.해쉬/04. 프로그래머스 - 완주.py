def solution(clothes):
    
    n = len(clothes)
    d = dict()
    for x in clothes:
        d[x[1]] = d.get(x[1], 0) + 1
    
    res = 1
    for val in d.values():
        res *= (val+1)
    
    return res -1
