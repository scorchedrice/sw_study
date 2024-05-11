#include <iostream>

using namespace std;

int main(void)
{
    const int num = 12;
    const int *ptr = &num;
    cout<<ptr<<endl;
    const int *(&ref) = ptr;
    // 포인터변수를 정의할건데, 그 변수는 참조자야
    cout<<ref<<endl;
    
    return 0;
}
