// 참조자를 활용해 다음 요구사항에 부합하는 함수를 각각 정의하라
// 1. 인자로 전달된 int형 변수 값을 1씩 증가시키는 함수
// 2. 인자로 전단된 int형 변수의 부호를 바꾸는 함수

#include <iostream>

using namespace std;

void myAdd(int &ref1, int &ref2)
{
    ref1 += 1;
    ref2 += 1;
}

void multiMinus(int &ref1, int &ref2)
{
    ref1 = ref1 * -1;
    ref2 = ref2 * -1;
}

int main(void)
{
    int val1 = 10;
    int val2 = 20;
    cout<<"기존 숫자:"<<val1<<","<<val2<<endl;
    myAdd(val1,val2);
    cout<<"1씩 증가:"<<val1<<","<<val2<<endl;
    multiMinus(val1, val2);
    cout<<"부호 변경:"<<val1<<","<<val2<<endl;
    // multiMinus(1,1);
    // Q2. 상수는 참조자를 선언할 수 없다!
    return 0;
}
