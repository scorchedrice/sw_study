// 판매원 급여 계산 프로그램
// 매달 50만원의 기본급 + 판매금액의 12%
// -1이 입력된 경우 반복문 종료

#include <iostream>

int main(void)
{
    int sell;
    sell = 0;
    while (true)
    {
        std::cout<<"판매금액: ";
        std::cin>>sell;
        if (sell == -1)
        {
            std::cout<<"종료"<<std::endl;
            break;
        }
        
        std::cout<<"이번달 급여: "<<50+sell*0.12<<"만원"<<std::endl;
    }
    


    return 0;
}