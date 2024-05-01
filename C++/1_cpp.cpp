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

