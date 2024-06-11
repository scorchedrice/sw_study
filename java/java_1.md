# Data Type
- 논리형: boolean(true/false)
- 문자형: char(2byte, null)
- 숫자형
  - byte(1byte, 0)
  - short(2byte, 0)
  - int(4byte, 0)
  - long(8byte, 0L)
  - float(4byte, 0.0f)
  - double(8byte, 0.0d)

# 형변환
- 묵시적(암묵적): 범위가 넓은 데이터 형으로,, 
- 명시적: 범위가 작은 데이터 형으로 ,, 라고 생각하자
## 형변환 방향성
byte => (short or char) => int(-21억~21억) => long(-10^9~10^9) => float(-10^38~10^38) => double(-10^308~10^308) ... 묵시적 방향성
### Example - 묵시적
  ```java
  byte b = 100;
  int i = b;
  // 해당 과정 문제 없음.
  ```
### Example - 명시적
  ```java
  int i = 100;
  // byte b = i; 불가!
  byte b = (byte) i;
  ```
# 연산자
## 단항 연산자 (항 하나)
- 증감 연산자 (++, --)
  - 전위형 (++i) : 먼저 증가(감소)시킨 후 그 값을 사용
  - 후위형 (--i) : 값을 사용한 이후 값을 증가(감소)
    ```java
    int a = 5;
    System.out.println(++a) // 5
    // 6
    ```
- string 비교는 equals() 사용
- 논리 연산자
  - &&: AND
  - ||: OR
  - !: NOT

# 조건문(if, switch)
- if는 python / javaScript와 크게 다르지 않음.
## switch
- 인자로 변수를 받고, 변수의 값에 따라 실행문 결정
  ```java
  if (수식) {
    case 값1:
      실행문 1;
      break;
    case 값2;
      실행문 2;
      break;
    default:
      실행문 C;
  }
  ```
# 반복문(for, while, do while)
## for
  for(초기화식; 조건식; 증감식;) {
    실행
  }
  - javaScript와 크게 다르지 않음.
## while 
  while (condition) {
    do something
  }
## do while
- while과 다르게 블록 내용을 먼저 수행하고 조건식을 판단한다. 그러니까 최소 한번은 무조건 수행한다는 이야기
```java
do {
  block content
} while (condition);
```
