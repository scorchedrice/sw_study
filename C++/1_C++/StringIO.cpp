#include <iostream>

int main(void)
{
    char name[100];
    char favorite[200];

    std::cout<<"당신의 이름은?: ";
    std::cin>>name;

    std::cout<<"가장 좋아하는 것은?: ";
    std::cin>>favorite;

    std::cout<<"내 이름은 "<<name<<"이고 ";
    std::cout<<favorite<<"를(을) 가장 좋아합니다"<<std::endl;

    return 0;
}
