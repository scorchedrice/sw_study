// ptr 변수가 가리키는 값이 바뀌도록 함수 짜기
#include <iostream>
using namespace std;

void mySwap(int *(&ptr1), int *(&ptr2))
{
    cout<<ptr1<<"|"<<&ptr1<<"|"<<*(&ptr1)<<endl;
    int *temp = ptr1;
    // ptr 변수 또한 메모리 주소를 가지고 있음. 이 값을 임시 저장
    ptr1 = ptr2;

    ptr2 = temp;
}

int main(void)
{
    int val1 = 10;
    int val2 = 20;
    int * ptr1 = &val1;
    int * ptr2 = &val2;
    cout<<"기존:"<<ptr1<<"|"<<ptr2<<endl;
    mySwap(ptr1, ptr2);
    cout<<"변경후:"<<ptr1<<"|"<<ptr2<<endl;
    return 0;
}
