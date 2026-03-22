#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    // 번호로 이름을 찾기 위한 벡터 (1번 인덱스부터 사용)
    vector<string> arr(n + 1);

    // 이름으로 번호를 찾기 위한 맵
    unordered_map<string, int> name_to_num;

    for (int i = 1; i <= n; i++) {
        string name;
        cin >> name;
        arr[i] = name;             // 인덱스(번호)에 이름 저장
        name_to_num[name] = i;     // 문자열(이름)을 Key로, 번호를 Value로 저장
    }

    // 검사해야 하는 문제들 입력
    vector<string> problems(m);
    for (int i = 0; i < m; i++) {
        cin >> problems[i];
    }

    // 답 구하기
    for (int i = 0; i < m; i++) {
        string problem = problems[i];
        
        // 첫 글자가 숫자인지 확인
        if (problem[0] >= '1' && problem[0] <= '9') {
            // 입력이 숫자인 경우, 벡터에서 인덱스로 바로 접근
            cout << arr[stoi(problem)] << "\n";
        } else {
            // 입력이 문자인 경우, 맵에서 Key(이름)로 바로 접근
            cout << name_to_num[problem] << "\n";
        }
    }

    return 0;
}