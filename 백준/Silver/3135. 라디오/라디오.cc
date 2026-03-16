#include <iostream>
#include <cmath>

using namespace std;

int main() {
    // abs() 함수:
    // 소괄호 안의 값의 절대값(=거리)을 구하는 함수

    // 입력처리
    int a, b;
    cin >> a >> b;
    
    int n;
    cin >> n;

    // distance : 첫번째 혹은 두번째 버튼만을 눌러서 B에 도착하는 횟수
    // 초기값은 A와 B 사이 거리
    int distance = abs(a - b);

    // success : 즐겨찾기 버튼 이용 여부를 저장하는 변수
    // 초기값은 사용X (False)
    bool success = false;

    for (int i = 0; i < n; i++) {

        // 즐겨찾기 버튼 입력 처리
        int button;
        cin >> button;

        // 만약 즐겨찾기 버튼과 B사이 거리가 A와 B사이 거리보다 가깝다면,
        if (abs(button - b) < distance) {
            distance = abs(button - b);  // distance 갱신
            success = true;              // 즐겨찾기 버튼 사용O
        }
    }

    // 출력 처리
    if (success) {             // 만약 즐겨찾기 버튼을 이용해야 한다면,
        cout << 1 + distance << "\n";  // 즐겨찾기 버튼 누르기(1회) + 첫 번째 혹은 두 번째 버튼을 눌러서 B에 도착(distance회)
    } else {                   // 만약 즐겨찾기 버튼을 이용하지 않는다면,
        cout << distance << "\n";      // 첫 번째 혹은 두 번째 버튼만을 눌러서 B에 도착(distance회)
    }

    return 0;
}