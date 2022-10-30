def check(x):
    for i in range(len(x)//2):
        if x[i] != x[len(x)-i-1]:
            print('no')
            return
        else:
            i += 1
    else:
        print('yes')

while True:
    n = input()
    if n == '0': break
    check(n)