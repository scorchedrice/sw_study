# C언어의 복습
## const의 의미
```cpp
const int num = 10;
// num을 상수화
const int * ptr1 = &val1;
// ptr1을 이용해서 val1의 값을 변경할 수 없음.
int * const ptr2 = &val2;
// 포인터 ptr2가 상수화된다.
const int * const ptr3 = &val3;
// 포인터 ptr3가 상수화 되었으며, ptr3를 이용해서 val3를 변경할 수 없음.
```
## 실행중인 프로그램의 메모리 공간
- 데이터 : 전역변수가 저장되는 영역
- 스택 : 지역변수 및 매개변수가 저장되는 영역
- 힙 : malloc 함수호출에 의해 프로그램이 실행되는 과정에서 동적으로 할당이 이뤄지는 영역 (내가 원할 때 넣고, 빼고싶을때 뺀다.)
- malloc & free : 메모리 공간 할당 함수 & 해제 함수

## Call-by-value & Call-by-reference
- 함수가 값에 의한 호출이냐 (value), 참조에 의한 호출이냐 (reference)
```cpp
// CallByReference
void SwapByRef(int * ptr1, int * ptr2)
{
    int temp = *ptr1;
    *ptr1 = *ptr2;
    *ptr2 = temp;
}
```

# 새로운 자료형 Bool
- true, false
- 둘 다 1바이트의 데이터로, 이들의 값이 각각 정수1과 0을 의미하는 것은 아니다. 하지만, 정수가 와야하는 위치에 오게된다면 각각 1과 0으로 변환이 된다.
```cpp
#include <iostream>

using namespace std;

int main(void)
{
	int num = 10;
	int i = 0;
	cout << "true:" << true << endl;
	cout << "false:" << false << endl;
	// 여기서 true, false는 숫자로 전환된 것을 의미

	cout << "1의 size:" << sizeof(1) << endl;
	cout << "true의 size" << sizeof(true) << endl;
	// 1은 4, true는 1 바이트의 데이터 확인 가능
	// 둘은 다른 데이터이다!!!!
	return 0;
}
```
# 참조자의 이해
```cpp
int num = 10

// 1.
int ref = num
// 2.
int &ref = num
// 1번, 2번 무엇이 다른가!
```
- 1번의 경우엔 새로운 메모리 주소에 ref를 할당하고 num의 정수값을 복사해온다.
- 2번의 경우엔 기존 num이 존재하는 메모리 주소에 ref 추가! (참조자, 접근할 수 있는 길 추가)
    - 쉽게말해 별명 추가!
## &의 기능 (메모리 주소 반환, 참조자)
```cpp
#include <iostream>

using namespace std;

int main(void)
{
	int num = 10;
	cout << "&num" << endl;
	cout << "num이 존재하는 주소 값 반환:" << &num << endl;
	// 메모리 주소를 반환!

	int &ref = num;
	// ref가 num의 메모리 주소를 바라보도록 참조자 기능!
	cout;

	cout <<"int &ref = num 이후 &ref 출력" <<&ref << endl;

	return 0;
}
```
### 포인터 변수
```cpp
int * ptr1 = &num
```
- 위 형태로 정의할 수 있으며, 메모리 주소를 가진다.
- 포인터 변수 또한 메모리 주소를 가지고 있다!

## 참조자의 선언 범위
- 상수 대상으로 참조자 선언은 불가능
- 참조자는 그냥 생성할 수 없다. 생성과 동시에 누군가를 참조해야 하며, NULL로 초기화 하는 것도 불가능하다.
- 변수의 성향을 지니는 대상이라면 참조자 설정 가능하다. 배열의 요소도 참조자 선언 가능! 포인터 변수 ptr, dptr도 참조자 선언 가능!

# 참조자와 함수
- 포인터 변수를 매개변수로 하는 함수는 CallByValue 함수일까 CallByReference일까?
  - CallByValue!, 포인터 변수 또한 메모리 주소 값을 가지고 있다.
## 굳이 CallByReference를 사용하는 이유는 무엇일까?
- CallByReference를 통해 함수 외부에 선언된 변수에 접근하기 용이하기 때문이다!
  - CallByValue의 경우 외부에 선언된 변수에 접근하기 쉽지 않음.
## 참조자를 활용한 CallByReference
```cpp
#include <iostream>

using namespace std;

// Reference Swap
void SwapByRef(int &ref1, int &ref2)
{
    int temp = ref2;
    ref2 = ref1;
    ref1 = temp;
}


int main(void)
{
    int var1 = 10;
    int var2 = 20;

    cout<<"BeforeSwap-var1,var2:"<<var1<<","<<var2<<endl;
    SwapByRef(var1, var2);
    cout<<"AfterSwap-var1,var2:"<<var1<<","<<var2<<endl;
    return 0;
}

```
