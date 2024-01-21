# Contents
1. Packing and Unpacking
2. Module
3. Library

# 1. Packing, Unpacking
## 1.1 Packing
- 여러 개의 값을 하나의 변수에 묶어서 담는 것
### Packing example
- 변수에 담긴 것들
```python
example_1 = 1, 2, 3
print(example_1) # (1, 2, 3)
```
- `*`을 활용
```python
 numbers = [1, 2, 3, 4, 5]
    a, *b, c = numbers
    
    print(a) # 1
    print(b) # [2, 3, 4]
    print(c) # 5
```
```python
print('hello') # hello
    
print('you', 'need', 'python') # you need python
```

# 2. Module
- 다른 프로그래머가 이미 작성해놓은 수천 수백만 줄의 코드를 사용하는 것으로 효율성을 위해 중요
- 한 파일로 묶인 변수와 함수의 모음
- .py로 작성된 파일
## 2.1 Module example
### math
```python
import math
    
print(math.pi)  # 3141592653589793
    
print(math.sqrt(4))  # 2.0
```

> python 내부 어딘가에 math.py가 저장되어 있다. 이를 import를 사용하여 불러올 수 있음.

## 2.2 Module 활용
### 1. import를 활용하기
1. import를 통해 module을 불러온다. 이 때 help(불러오는 모듈)를 통해 모듈에 무엇이 들어있는지 확인 가능
2. 불러온 module 뒤에 `.`을 활용하여 module을 사용한다.
### 2. from 절을 활용하기
```python
from math import pi, sqrt
print(pi)
print(sqrt(4))
```
- 이처럼 불러오면 math 내에 있는 pi와 sqrt를 직접 불러와 `.`을 사용하지 않고 바로 함수 사용 가능

> 두 방법 모두 사용해도 상관 없으나 첫번째 방법을 사용하는 것이 권장된다. 이는 서로 다른 모듈에서 같은 이름의 변수/함수 등이 발생하는 문제를 방지할 수 있기 때문이다.
>> ```python
>> from math import sqrt
>> from my_math import sqrt
>> #이 경우 중복의 문제 발생, 하단 sqrt가 사용

## 2.3 Module 만들고 활용하기
1. Module로 활용할 .py를 만든다.
2. 이를 import하여 활용한다.
```python
# my_math.py
def add(x,y):
    return x+y
```
```python
# module_prac.py
import my_math
print(my_math.add(1,2)) # 3
```
# 3. Python Standard Library (파이썬 표준 라이브러리)
- python과 함께 제공되는 모듈과 패키지들의 모음

    [참고 문서](https://docs.python.org/ko/3/library/index.html)
## 3.1 Package
- 관련된 모듈들을 하나의 디렉토리에 모아 놓은 것.
### Package 활용하기
 ```markdown
    📦...
     ┣ 📜sample.py
     ┣ 📂my_package
     ┃ ┣ 📂math
     ┃ ┃ ┗ 📜my_math.py
     ┃ ┣ 📂statistics
     ┃ ┃ ┗ 📜tools.py
```
```python
from my_package.math import my_math
from my_package.statistics import tools


print(my_math.add(1, 2))
print(tools.mod(1, 2))
```
- Package 안에 Package인 경우 위와 같이 import

### PSL 내부 패키지 & 외부 패키지
---
#### PSL 내부 패키지
- 설치 없이 import로 활용 가능
#### 외부 패키지
- pip로 설치하여 활용 가능
- PyPI(Python Package Index)에 저장된 외부 패키지들을 설치
> https://pypi.org/
```python
#외부 패키지 설치 예시
pip install request
```
하면 설치 진행
```
Collecting requests
  Downloading requests-2.31.0-py3-none-any.whl (62 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 62.6/62.6 KB 670.9 kB/s eta 0:00:00  
     .
     .
     .
```
