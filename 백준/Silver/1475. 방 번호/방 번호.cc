#include <iostream>
#include <string>
#include <vector>
#include <algorithm> // max_element를 사용하기 위한 라이브러리

using namespace std;

int main() {
    // 다솜의 방 번호(N)를 문자열로 입력 받습니다.
    string n;
    cin >> n;

    // 0~9 숫자의 개수를 저장할 벡터를 선언합니다.
    vector<int> nums_count(10, 0);

    // 다솜의 방 번호를 처음부터 끝까지 순회하며 필요한 숫자 개수를 저장합니다.
    for (char num : n) {
        nums_count[num - '0'] += 1;
    }

    // 6과 9는 뒤집어서 사용할 수 있는 것을 처리합니다.
    // 예시1) 6과 9가 합쳐서 총 5개 필요하다면 3세트가 필요합니다.
    // 예시2) 6과 9가 합쳐서 총 6개 필요하다면 3세트가 필요합니다.

    // 정수 나눗셈(/)은 나머지를 버리기 때문에, 
    // 총 필요한 6과 9개수에 1을 더하고 2로 나누어 주면, 
    // 최소한으로 필요한 세트를 구할 수 있습니다.
    int temp = (nums_count[6] + nums_count[9] + 1) / 2;
    nums_count[6] = temp;
    nums_count[9] = temp;

    // 필요한 세트의 개수의 최솟값(벡터의 최댓값)을 출력합니다.
    cout << *max_element(nums_count.begin(), nums_count.end()) << "\n";

    return 0;
}