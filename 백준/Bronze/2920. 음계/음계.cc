#include <iostream>
using namespace std;

int main()
{
    // 음계 8개를 저장할 배열과 상태를 체크할 변수 선언
    int arr[8];
    int asc = 0; // 오름차순 확인용 변수
    int dsc = 0; // 내림차순 확인용 변수

    // 반복문을 통해 8개의 숫자를 입력받고 순서를 확인한다.
    for (int i = 0; i < 8; i++)
    {
        cin >> arr[i];

        // 현재 입력된 숫자가 순서대로(1, 2, 3...) 들어오는지 확인
        if (arr[i] == i + 1)
            asc += 1;
        // 현재 입력된 숫자가 역순으로(8, 7, 6...) 들어오는지 확인
        else if (arr[i] == 8 - i)
            dsc += 1;
    }

    // 조건문을 통해 카운트 결과에 따라 결과값을 출력한다.
    // 8개 음이 모두 순서대로라면 ascending
    if (asc == 8)
        cout << "ascending";
    // 8개 음이 모두 역순이라면 descending
    else if (dsc == 8)
        cout << "descending";
    // 둘 다 아니라면 mixed
    else
        cout << "mixed";

    return 0;
}