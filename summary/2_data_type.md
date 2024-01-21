# Contents
```
1. Numeric Type
2. Sequence Type (str, list, tuple, range)
3. Non-Sequence Type (dict, set)
4. Other Type
```

# 1. Numeric Type
## 1.1 int (정수)
```
binary(2진수) : 0b
octal(8진수) : 0o
hexadecimal(16진수) : 0x
```

## 1.2 float (실수 자료형)
- 컴퓨터는 2진수를 사용하기에 소수의 경우 무한대 숫자로 표현될 수 있다. 즉, 소수의 경우 그대로 저장할 수 없기에 사람이 사용하는 10진법의 근삿값만 표시한다.

**Example**
```python
a = 3.2 - 3.1
b = 1.2 - 1.1
if a == b:
    print('Same')
else:
    print('Difference')
# 이를 실행하면 Difference가 출력됨
# 즉, 정확한 값을 저장하지 않고 근삿값을 표시한다는 말
# 이를 해결하기 위해선 a, b의 차이가 몇 이하인 경우 같다고 취급한다! 와 같은 조건을 걸어 해결 가능 (오차 고려)
```
# 2. Sequence Type (str, list, tuple, range)
- 여러 개의 값들을 순서대로 나열하여 저장하는 자료형 (str, list, tuple, range)

**Sequence Type의 경우 순서를 가지기에 다음을 활용할 수 있다.**

2.1 Indexing - [a] : a의 index를 가진 것 찾기

2.2 Slicing - [a:b], [:b], [a:], [a:b:z].. : index 범위, step을 지정하여 그 요소를 찾기

---
|positive index|negative index|
|:---|---:|
|0,1,2,3, ...|... -3,-2,-1|
---
2.3 Length : 해당 Sequence Type의 길이(개수)

Iteration : 반복

## 2.1 str(문자열)
- 문자들의 **순서**가 있는 **변경 불가능**한 Sequence Type data
- Escape Sequence를 활용하여 줄 변경 등 입력 가능
    |예약문자|내용(의미)|
    |:---:|:---:|
    |`\n`|줄 바꿈|
    |`\t`|탭|
    |`\\`|백슬래시|
    |`\'`|작은따옴표|
    |`\"`|큰따옴표|
- f-string 을 활용하여 python의 표현식 값을 삽입할 수 있다.
```python
bugs = 'roaches'
counts = 13
area = 'living room'

print(f'Debugging {bugs} {counts} {area})

# Debugging roaches 13 living room
```

## 2.2 list
- 여러 개의 값을 순서대로 저장하는 변경 가능한 Sequence Type
- []로 표기하며 어떤 자료형도 저장할 수 있다.
- indexing, slicing, len 모두 활용 가능
- list 데이터는 가변!

## 2.3 tuple
- 여러 개의 값을 순서대로 저장하는 **변경 불가능한** Sequence 자료형
- ()로 표기하며 어떤 자료형도 데이터로 저장 가능
- indexing, slicing, len 모두 활용 가능
- 불변 특징을 가지기에 안전하게 여러개의 값을 전달, 그룹화, 다중 할당 하는 것에 활용 많다. python 내부 동작에서 사용 많음

### list 와 tuple의 차이
- 비슷한 성질을 가지나 표현법과 가변/불변이 큰 차이

## 2.4 range
- 연속된 정수 시퀀스를 생성하는 변경 불가능한 자료형
```python
range(n)
# 0부터 n-1까지의 숫자 시퀀스
range(n,m)
# n부터 m-1까지의 숫자 시퀀스
list(range(n,m))
# 숫자 시퀀스를 리스트로 할당
```

## Sequence Type 중요 차이점
가변 : list

불변 : str, tuple, range

---
## 3. Non-Sequence Type (dict, set)
- ***Non Sequence이기에 순서로 접근할 수 없다!!!!***
### 3.1 dict
- {}안에 key - value로 구성된다.
- key는 변경 불가능한 자료형만 사용 가능하다

    |변경 O|변경 X|
    |:---:|:---:|
    |list ...|str, int, float, tuple, range ...|

- value는 모든 자료형 사용 가능
- value는 변경 가능하다.
- key를 통해 value에 접근 가능
- 중복된 key 가질 수 없다.

## 3.2 set
- 순서와 중복이 없는 변경 가능한 자료형
- {}로 표기한다.
- 집합의 개념
```python
my_set_1 = {1,2,3}
my_set_2 = {3,6,9}
print(my_set_1 + my_set_2)
# {1,2,3,6,9}
```

# 4. Other Type
## 4.1 None
## 4.2 Boolean
- `True`, `False` 를 표현하는 자료형
### Boolean 사용처
- 비교, 논리 연산의 평가 결과로 사용됨
- 주로 조건 / 반복문과 함께 활용

# 정리!
|     컬렉션    	|     변경 가능 여부    	|     순서 여부    	|          	|
|:-------------:	|:---------------------:	|:----------------:	|:--------:	|
|       str     	|            X          	|         O        	|  시퀀스  	|
|      list     	|            O          	|         O        	|  시퀀스  	|
|      tuple    	|            X          	|         O        	|  시퀀스  	|
|       set     	|            O          	|         X        	| 비시퀀스 	|
|      dict     	|            O          	|         X        	| 비시퀀스 	|

![image](https://github.com/ragu6963/TIL/assets/32388270/b6dca7db-4a13-4e75-843b-cbc8badf3691)