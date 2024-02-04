# Contents
1. Function
2. 매개변수(Parameter)와 인자(Argument)
3. Scope
4. 재귀함수

# 1. Function
- 재사용성, 가독성, 유지보수성 목적

구성 형태는 다음과 같다.
```python
def function_ex(x,y):
    return x + y
# def로 정의 시작, def 뒤에 함수 이름 작성 (매개변수 정의)
```

## 1.1 내장 함수 (Built-in)
`map(func, iterable)`
> map의 경우 iterable에 있는 모든 변수에 func을 적용하여 map object로 반환한다. 여기서 iterable은 반복이 가능한 sequence 의미.

```python
# map Example
#example1
numbers = [1,2,3]
result = map(str, numbers)
print(result) # <map object at 0x00000...>
print(list(result)) # ['1','2','3']

#example2
#[input] 1 2 3 4 5
numb = input().split() # 입력값을 list화
print(numb) # ['1','2', ...]
print(map(int, numb)) # map object ~~
print(list(map(int, numb))) # [1,2,3,4,5]
```

`zip(*iterables)`
> iterable들을 모아 tuple을 원소로 하는 zip object를 반환한다.
```python
#example1
girls = ['jane', 'ashley']
boys = ['peter', 'jay']
pair = zip(girls, boys)

print(pair) # <zip object at 0x000001C76DE58700>
print(list(pair)) # [('jane', 'peter'), ('ashley', 'jay')]
```
`lambda`
> 이름이 없이 정의되는 익명함수
```python
#간단한 계산등을 위해 활용
#example1
addition = lambda x, y: x+y
result = addition(3,4)
print(result) # 7
```
---
이 외에도 `abs`, `print` 등 존재

# 2. 매개변수(Parameter)와 인자(Argument)
## 2.1 위치인자 (Positional Arg.)
- 함수 호출 시 위치에 따라 전달되는 인자
- 위치인자는 호출 시 반드시 값을 전달해야
```python
def greet(name, age):
        print(f'안녕하세요, {name}님! {age}살이시군요.')
        # name, age의 인자 위치가 바뀌면 이상하게 나올 수 있음. 개수가 안맞아도
```
## 2.2 기본 인자 값 (Default Arg. Values)
- 함수 정의에서 매개변수에 기본 값을 할당하는 것
- 함수 호출 시 인자를 전달하지 않으면, 기본값이 매개변수에 할당됨
```python
def greet(name, age=30):
        print(f'안녕하세요, {name}님! {age}살이시군요.')
        #age=30으로 해서 개수가 모자라게 입력하더라도 기본값을 정상 출력.
```
## 2.3 키워드 인자 (Keyword Arg.)
- 함수 호출 시 인자의 이름과 값을 함께 전달하는 인자
- 위치에 상관없이 이를 사용하면 특정 매개변수에 값을 할당할 수 있다.
```python
greet(name='Dave', age=35)  # 안녕하세요, Dave님! 35살이시군요.
```
## 2.4 임의의 인자 목록 (Arbitrary Arg. lists)
- 정해지지 않은 개수의 인자를 처리하는 인자
- 함수 정의 시 매개변수 앞에 `*`를 붙여 사용하며, 여러개의 인자를 tuple로 처리
```python
def calculate_sum(*args):
        print(args)
        total = sum(args)
        print(f'합계: {total}')

    print(calculate_sum(1, 2, 3))
    # 6
```
## 2.5 임의의 키워드 인자 목록 (Arbitrary Keyword Arg. lists, kwarg)
- 정해지지 않은 개수의 인자 처리
- `**`를 붙여 사용, 여러개의 인자를 dictionary로 묶어 처리
```python
    def print_info(**kwargs):
        print(kwargs)


    print_info(name='Eve', age=30) # {'name': 'Eve', 'age': 30}
```
# 3. Scope(Local, Global)
![image](https://github.com/ragu6963/TIL/assets/32388270/15b4f0c6-7f21-4986-8349-fd8740e49573)

- 수명 주기와 관련
- 외부 Scope의 변수는 내부 Scope에서 사용 가능하나 그 반대는 불가능하다. (LEGB Rule)
## global 선언
- 변수의 Scope를 전역 범위로 지정
- 함수 내 Local Scope에서 전역 변수를 수정하기 위해 활용
```python
a = 1
b = 2


def enclosed():
    a = 10
    c = 3

    def local(c):
        print(a, b, c)  

    local(500) 
    # 10 2 500, 함수가 실행될 때, c값(500)입력, a값은 상위에 존재하는 10, b는 global에 존재하는 2
    print(a, b, c)  
    # 10 2 3


enclosed()
print(a, b) # Local에 있는 값 무시하고 Global에 있는 값 출력 
```

# 4. 재귀함수
- 함수 내부에서 자기 자신을 호출하는 함수
- 일정 조건을 충족하면 멈추도록 설계해야 (if 활용)
```python
#factorial
def my_fac(n):
    if n == 0:
        return 1
    return n*my_fac(n-1)
```