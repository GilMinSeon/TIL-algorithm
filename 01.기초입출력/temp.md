## Do it! 자료구조와 함께 배우는 알고리즘 입문(파이썬 편) 01-2 반복하는 알고리즘 발췌

## 1) 1부터 n까지 정수의 합 구하기 

### 1-1) while문
```python
n = int(input())

sum = 0
i = 1

while i <= n: # i가 n보다 작거나 같은 동안 반복
							sum += i
	i += 1

print(sum)
```

### 1-2) for문
```python
n = int(input())

sum = 0
for i in range(1, n+1):
	sum += i

print(sum)
```

## 2) a부터 b까지 연속하는 정수의 합 구하기
- 연속하는 정수의 합을 구할 때 시작하는 값이 1이 아닌 정수를 입력받았다면 range() 함수에 전달할 시작값과 끝값을 오름차순으로 정렬해야 한다.

### 2-1) sum값 출력
```python
a = int(input())
b = int(input())

if a > b: 
	a, b = b, a # a와 b를 오름차순으로 정렬

sum = 0
for i in range(a, b+1):
	sum += i
  
print(sum)
```

### 2-1) 합을 구하는 과정과 sum값 출력 

- 안 좋은 예
```python
sum = 0
for i in range(a, b+1):
	if i < b:
		print(f'{i} + ', end='')
	else:
		print(f'{i} = ', end='')
	sum += i

print(sum)
```

- 좋은 예
```python
sum = 0
for i in range(a, b):
	print(f'{i} + ', end='')
	sum += i

print(f'{b} = ', end='')
sum += b


for i in range(a,b):
	ab.   
print(sum)
```




