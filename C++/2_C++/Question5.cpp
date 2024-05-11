// 라이브러리 호출, 이를 활용한 프로그램 작성
// strlen, strcmp (0인경우 동일값, 다른 문자인 경우 ASCII 차이 반환)
#include <iostream>
#include <cstring>

using namespace std;

int main(void)
{
    cout<<"문자열 놀이"<<endl;
    char myInput1[100];
    cout<<"단어1 입력: ";
    cin.getline(myInput1,100,'\n');

    char myInput2[100];
    cout<<"단어2 입력: ";
    cin.getline(myInput2,100,'\n');

    if (strcmp(myInput1, myInput2) == 0) {
        cout<<"동일한 단어 입력!"<<endl;
    } else {
        cout<<"다른 입력을 하셨군요!"<<endl;
    };

    cout<<"문자열의 길이 비교:";
    cout<<"단어1: "<<strlen(myInput1)<<"|"<<"단어2: "<<strlen(myInput2)<<endl;
    
    return 0;
}
