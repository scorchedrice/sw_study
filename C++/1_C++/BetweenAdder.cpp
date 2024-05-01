#include <iostream>
// 지역변수의 선언
int main(void)
{
    int val1, val2;
    // val1, val2 선언
    int result=0;
    // 결과 선언

    std::cout<<"두 개의 숫자 입력!: ";
    std::cin>>val1>>val2;
    
    if (val1<val2)
    {
        for(int i = val1+1; i<val2; i++)
            result += i;
    }
    else
    {
        for(int i=val2+1; i<val1; i++)
            result+=i;
    }

    std::cout<<"두 수 사이의 정수 합: "<<result<<std::endl;

    return 0;
}