// 구구단 출력
#include <iostream>

int main(void)
{
    /* code */
    int number;
    std::cout<<"몇 단을 알려드릴까요?";
    std::cin>>number;

    for (int i = 1; i < 10; i++)
    {
        /* code */
        std::cout<<number<<"x"<<i<<"="<<number*i<<std::endl;
    };
    
    return 0;
}
