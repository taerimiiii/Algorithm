#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

int main() {
    // n과 m 한 줄 공백 입력 처리
    int n, m;
    cin >> n >> m;

    // 맵 자료형을 이용한 집합S 입력 처리
    unordered_map<string, bool> s_set;
    for (int i = 0; i < n; i++) {
        string k;
        cin >> k;
        s_set[k] = true;     // 문자열을 key로 두고 value를 True로 준다.
    }

    // 정답을 저장할 변수 선언
    int answer = 0;

    // 답 구하기
    for (int i = 0; i < m; i++) {
        string target;
        cin >> target;       // 검사해야 하는 문자열 입력
        if (s_set.find(target) != s_set.end()) { // 타겟 문자열이 S집합에 있다면
            answer += 1;     // 답+1
        }
    }

    // 출력처리
    cout << answer << "\n";

    return 0;
}