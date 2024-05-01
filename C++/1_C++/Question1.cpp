// 정수 5개를 받고, 그 합을 출력하는 프로그램
#include <iostream>

int main(void)
{
    /* code */
    int val1;
    int val2;
    int val3;
    int val4;
    int val5;
    std::cout<<"1번째 숫자 입력: ";
    std::cin>>val1;
    
    std::cout<<"2번째 숫자 입력: ";
    std::cin>>val2;

    std::cout<<"3번째 숫자 입력: ";
    std::cin>>val3;

    std::cout<<"4번째 숫자 입력: ";
    std::cin>>val4;

    std::cout<<"5번째 숫자 입력: ";
    std::cin>>val5;

    std::cout<<"합계: "<<val1+val2+val3+val4+val5<<std::endl;
    return 0;
}
