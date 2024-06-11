# Array (1차원)
## 배열의 선언
- iArr(int type), cArr(char type), nArr(boolean type), strArr(String type), dateArr(Date type)
- 선언은 int[] iArr;, char[] cArr; ... 의 방법 활용

## 배열의 생성, 초기화
- 자료형[] 배열이름 = new 자료형[길이]; // 배열 생성, 자료형의 초기값으로 초기화
- 자료형[] 배열이름 = new 자료형[] {값1, 값2, 값3, 값4}; // 배열 생성 및 값 초기화
- 자료형[] 배열이름 = {값1, 값2, 값3, 값4}; // 선언과 동시에 초기화

### 배열 생성 example
```java
int intArray [] = {1,3,5,7,9};
// intArray 생성 과정

for (int x : intArray) {
  System.out.println(x);
} // intArray 순회 과정 방법1
for (int i = 0; i<intArray.length; i++) {
  int x = intArray[i];
  System.out.println(x);
} // intArray 순회 과정 방법2 .. python 반복문의 index활용과 유사
```

### 배열 응용 example (최대 최소 찾기)
```java
int[] intArray = {3, 27, 13, 8, 235, 7, 22, 31}; // 주어진 배열

int min = 1000;
int max = 0;

for (int i = 0; i<intArray.length; i++) {
  int x = intArray[i]
  if (x > max) {
    max = num;
  }
  if (x < min) {
    min = num;
  }
} // 반복문을 활용한 최대 최소 찾기
```
- 물론 다른 방법으로 구할수 있긴함.
