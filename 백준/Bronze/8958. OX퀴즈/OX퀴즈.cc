#include <iostream>
#include <string>

using namespace std;

int main() {
    // 빠른 입출력을 위한 설정 (sys.stdin.readline과 유사한 효과)
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // N 입력 처리
    int n;
    cin >> n;

    for (int j = 0; j < n; j++) {

        // OX 문자열 입력 처리
        string ox;
        cin >> ox;

        // 필요한 변수 선언
        int ox_len = ox.length();    // OX 문자열의 길이
        int count = 0;               // 연속된 O의 개수
        int score = 0;               // 총 점수

        // for문을 이용하여, 입력 받은 OX 문자열의 앞에서부터 순서대로 탐색한다.
        for (int i = 0; i < ox_len; i++) {

            // 만약 이번 문자가 O 이라면
            if (ox[i] == 'O') {
                count += 1;      // 연속된 O의 개수 + 1
                score += count;  // 총 점수 갱신
            }
            
            // 만약 이번 문자가 X 이라면
            else {
                count = 0;       // 연속된 O의 개수 초기화
                                 // X 이므로 총 점수에 더해지는 점수는 없음
            }
        }
        
        // 구한 총 점수를 출력 처리
        cout << score << "\n";
    }

    return 0;
}