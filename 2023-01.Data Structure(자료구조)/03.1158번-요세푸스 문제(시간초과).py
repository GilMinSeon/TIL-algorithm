n, k = map(int, input().split())

# idea -> 1~n까지의 배열을 만들어서 k가 아니면 pop해서 append, k면 pop

q = [i for i in range(1, n+1)]
answer = []

idx = 1
while len(q) != 1:
    print(idx)
    if (idx % k) == 0:
        answer.append(q.pop(0))
    else:
        q.append(q.pop(0))
    idx += 1

# print('<', end = '')
# for x in answer:
#     if x == answer[-1]:
#         print(x, end='>')
#     else:
#         print(x, end=', ')

#print(', '.join(answer))

print('<', end='')
print(*answer, sep=', ', end='')
print('>')

# 계속 시간초과...