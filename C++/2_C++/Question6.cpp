#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main(void)
{
    srand(time(NULL));
    // srand: 난수표의 시드를 바꾸는 역할
    // time(NULL): 시간에 따라 다른 값을 가지기에, 난수표를 시간에 맞춰 변경
    int test = rand();
    cout<<test%101<<endl;
    // 101로 나눈 나머지를 출력해 1~100의 숫자 출력
    return 0;
}
