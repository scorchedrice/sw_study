// 이름, 전화번호 입력 후 출력
#include <iostream>

int main(void)
{
    /* code */
    char name[100];
    char phone[200];

    std::cout<<"이름 입력: ";
    std::cin>>name;
    
    std::cout<<"휴대폰 번호 입력: ";
    std::cin>>phone;

    std::cout<<"이름: "<<name<<" 전화번호: "<<phone<<std::endl;
    return 0;
}
