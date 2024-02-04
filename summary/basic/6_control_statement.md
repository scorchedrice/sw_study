# Contents
1. Conditional Statement(if)
2. Loop Statement(for, while)

# 1. 조건문(Conditional Statement)
- 해당 조건이 True라면, 그 조건 내의 Code Block을 실행한다.
- `if`, `elif`, `else`
## `if`
```python
if 표현식:
    Code block
elif 표현식:
    Code block
else:
    Code block
```
# 2. 반복문(Loop Statement)
- 주어진 Code Block을 여러번 반복해서 실행하는 구문
1. `for` 특정 작업을 반복 수행
2. `while` 주어진 조건이 참인 동안 반복 실행
### 반복 가능한 객체 (Iterable)
- 반복문에서 순회할 수 있는 객체
- Sequence 객체, dict, set ..
## 2.1 `for`
- 임의의 Sequence (str, tuple, list, range ...) 항목들을 그 시퀀스에 들어있는 순서대로 반복.
- 반복 횟수가 정해져 있음 (Sequence 내 요소에 따라)

```python
# for
for 변수 in 반복 가능한 객체:
    Code Block
```
## 2.2 `while`
- 주어진 조건식이 True인 동안 코드를 반복 실행 (즉, 조건식이 False가 될 때 까지 반복)
- 반드시 종료 조건이 필요하다!
```python
# while
while 조건:
    Code block
```
---
#### `for` ? `while` ?
- 반복 횟수가 명확한 경우 (list, tuple, str 과 같은 Sequence) `for`!
- 반복 횟수가 불명확한 경우, 조건에 따라 반복을 종료해야 하는 경우 `while`!

## 2.3 반복 제어
- `for`문과 `while`문은 매 반복마다 본문 내 모든 코드를 실행하지만, 상황에 따라 일부만 실행하는 것이 필요한 경우 있기에 제어할 수 있어야 한다.
- `break` : 반복을 즉시 중지
- `continue` : 다음 반복으로 건너뜀
#### `break`, `continue` 주의사항
- 너무 많이 쓰면 가독성 저하
- `if`문 활용, ==을 !=로 바꾸는 등의 방법을 활용

## 2.4 List Comprehension
- 간결하고 효율적인 리스트 생성 방법
```python
[expression for 변수 in iterable]

list(expression for 변수 in iterable)
```

```python
# Example1
numb = [1,2,3,4,5]
squared_numb = [num**2 for num in numb]

#Example2 (짝수만)
numb = [1,2,3,4,5]
squared_numb = [num**2 for num in numb if num%2 ==1]
```
- 하지만 `for` 내부에 `append`를 사용하는 리스트 형성 과정에 비해 가독성이 떨어진다는 문제점이 있어 남용은 자제해야 한다.

## `pass`
- 아무런 동작 안한다.
1. 미완성 부분에 활용하여 Error 방지 목적
2. 조건문에 활용

## `enumerate`
- index를 같이 출력할 수 있다.