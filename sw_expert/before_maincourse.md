## 1. 가위바위보
#### 1 : 가위, 2 : 바위, 3: 보
#### 승리 인원을 결과로 표시하도록 할 것
#### 입력은 3 2, 1 2 등으로 입력
```
a, b = map(int, input().split())
def game():
    if (a == 1 and b == 3) or (a == 2 and b ==1) or (a == 3 and b == 2):
        print('A')
    else:
        print('B')
game()
```
#### `input().split()`
- `input()` : 뭘 입력할래
- `.split()` : 입력한 것을 쪼개 무엇을 기준으로

## 2. 각 자리수 더하기
#### ex)1234의 경우 10이 나오도록
```
number = int(input())
a = number // 1000
b = (number - a*1000) // 100
c = (number - (a*1000 + b * 100)) // 10
d = number - (a*1000 + b * 100 + c * 10)
e = a+b+c+d
print(e)
```
`%` : 나머지

`//` : 몫
## 3. N개의 값 중 중간값 찾기
```N = int(input())
read_data = list(map(int, input().split()))
read_data.sort()
middle_index = N//2
print(read_data[middle_index])
```
***편견 때문에 오래 걸린 문제***
```문제에서 주어진 것은 input
199
12 3 4 5 ...
```

이런식으로 주어지면 한번에 복사해서 입력하는 줄 알았는데,
1. 199 enter
2. 12 3 4 5 ... enter

이런식이었음.
다음부터는 이런 실수 없도록 할 것.

`sort()` : 배열

`list(map(int, input().split()))`:default (공백)을 기준으로 분리, 이후 list화

## 4. 숫자 배열의 반복 속 가장 큰 수 찾기
주어진 input
```
3 
3 17 1 39 8 41 2 32 99 2
22 8 5 123 7 2 63 7 3 46
6 63 2 3 58 76 21 33 8 1
```
code
```
case = int(input())
max1 = max(map(int, input().split()))
print('#1', max1)
max2 = max(map(int, input().split()))
print('#2', max2)
max3 = max(map(int, input().split()))
print('#3', max3)
```

- 이 내용을 반복문으로 해결할 순 없나? 고민해보기

## 5. list 중 홀수만 더한 값 나타내기
주어진 input
```
3
3 17 1 39 8 41 2 32 99 2
22 8 5 123 7 2 63 7 3 46
6 63 2 3 58 76 21 33 8 1   
```
code
```
case = int(input())
list_1 = list(map(int, input().split()))
odd_1 = [num for num in list_1 if num % 2 != 0]
list_2 = list(map(int, input().split()))
odd_2 = [num for num in list_2 if num % 2 != 0]
list_3 = list(map(int, input().split()))
odd_3 = [num for num in list_3 if num % 2 != 0]
print('#1', sum(odd_1))
print('#2', sum(odd_2))
print('#3', sum(odd_3))
```
- 반복문 고민해보기