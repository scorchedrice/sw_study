# 1-1강
# 실습 예시를 보며 학습하기!
```cpp
// Example
#include <iostream>
// 입출력을 위한 헤더파일의 선언

int main(void)
{
    int num=20;
    std::cout<<"HelloWorld"<<std::endl;
    // std::endl - 개행 명령어구나
    std::cout<<"Hello "<<"World!"<<std::endl;
    std::cout<<num<<' '<<'A';
    // 출력의 기본 구성은 이런 방식이구나.
    std::cout<<' '<<3.14<<std::endl;
    return 0;
}
```
- 완전이해는 뒤에서 가능하니, 관찰하도록 하자.

# 데이터를 입력받는 방법
```cpp
#include <iostream>

int main(void)
{
    int val1;
    std::cout<<"숫자 입력 첫번째: ";
    // "숫자입력 ... "의 문자열을 console out으로
    std::cin>>val1;
    // console input으로 받은 것을 화살표방향 (val1)을 향해 할당
    int val2;
    std::cout<<"숫자 입력 두번째: ";
    std::cin>>val2;
    int result = val1 + val2;
    std::cout<<"두 수의 합: "<<result<<std::endl;
    return 0;
}
```
- int로 val1이라는 변수 선언
- 이후 cin>>val1을 통해 숫자를 입력받는구나

## 데이터를 입력받는 방법 - 여러개의 데이터
- BetweenAdder.cpp 참고

## while, for
- while (condition)
- for (int i = 0; i < 10; i++)
    - i를 0으로 정의한 후 이를 하나씩 더하면서 10인경우 종료

# 매개변수의 디폴트 값
- 함수를 정의할 때, 만약 아무 값도 전달되지 않는다? 이 때 전달될 매개변수의 값 정의
- 디폴트 값의 선언은 함수의 선언시 적혀 있어야 한다. (정의X)
- 일부만 디폴트값을 설정해도 괜찮다.
  - 하지만 전달되는 인자는 좌측부터 채워지므로, 디폴트 값은 오른쪽에서 부터 채워야 한다!
    ```cpp
    int testFunc(int num1=10, int num2=20, int num3) {...}
    // 이 경우 num3에만 변수를 넘겨주기 쉽지 않음!
    // testFunc(10) 은 num1에만 변수를 넘겨준 셈
    ```

# 인라인 함수
- 인라인화 되어 성능의 향상으로 이어질 수 있으나, 복잡한 함수 정의엔 한계가 있다. (기존 매크로함수의 특징)
- 이 장점을 취하고 단점을 최소화 하기 위한 C++의 함수 정의 : 인라인 함수
- 인라인선언은 컴파일러에 의해 처리된다(매크로함수는 선행처리). 디버깅이 용이하다.

## 그렇다면 매크로함수는 왜 존재하나
- 매크로 함수는 자료형에 독립적이다! 자료형을 명시해야하는 인라인 함수와 비교할 땐 큰 장점
  - 인라인 함수는 자료형 별로 함수가 오버로딩 되어야 매크로 함수처럼 호출될 수 있다.

# 이름공간 (name-space)
- A, B, C가 과제를 수행할 때, 함수명이 겹친다면 ..?
  - 누가 작성했는지 명시할 수 있다면! 충돌 문제를 막을 수 있다.
    - 이를 이름 공간이라고 한다.
```cpp
#include <iostream>
namespace Aname
{
	void aFunc(void)
	{
		std::cout << "A" << std::endl;
	}
}

namespace Bname
{
	void aFunc(void) 
	{
		std::cout << "B" << std::endl;
	}
}

int main(void)
{
	Aname::aFunc();
	Bname::aFunc();
    // A
    // B
	return 0;
}
```
- 같은 이름공간 내에 존재하는 함수들간 함수를 호출할 땐, 이름 공간을 명시하지 않고 호출할 수 있다.
- 이름공간은 중첩할 수 있다.
```cpp
// example
namespace Parent
{
    namespace SubOne
    {
        int num=3;
        // Parent::SubOne::num
    }
}
```
- std::endl, std::cout ... 
  - std 이름 공간에 있는 endl, cout을 가져오는구나

## using을 통한 이름공간의 명시
- using std::cin;
  - cin으로 std 이름공간의 cin을 가져올 수 있음.
- using namespace std;
  - std 내 존재하는 것들을 이름공간의 선언 없이 접근하겠다 선언하는 것.
- 이를 남용하면, 이름 충돌을 막기 위한 노력을 무의미하게 만든다. 따라서 제한적 사용이 필요.

## 이름공간의 별칭 지정
- 만약 AAA::BBB::CCC 로 계속 접근해야 한다?
  - 별칭을 지정할 순 없나?
    ```cpp
    namespace ABC = AAA::BBB::CCC;
    ```
    - 이를 통해 별칭 선언 가능!
    - ABC:: 으로 접근 가능.

## 전역변수 접근
- 함수를 정의할 때, 지역변수와 전역변수가 동일한 경우 다음을 통해 전역변수에 접근 가능하다.
```cpp
int val = 100;

int myFunc(void):
{
    int val = 50
    val += 5 // 지역변수 val 55
    ::val += 5 // 전역변수 val 105
}
```
