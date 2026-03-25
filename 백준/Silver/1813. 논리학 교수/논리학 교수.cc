#include <iostream>
#include <vector>

using namespace std;

int main() {
    // 입력 처리
    int n;
    cin >> n;

    vector<int> speech(n);
    for (int i = 0; i < n; i++) {
        cin >> speech[i];
    }

    // 각 숫자(주장)가 몇 번 나왔는지 개수를 세어두기 위한 배열 선언.
    vector<int> counts(n + 1, 0);

    for (int i = 0; i < n; i++) {
        // 전체 말의 개수(n)보다 큰 숫자를 부른 경우, 
        // 논리적으로 절대로 참이 될 수 없으므로 넘어감.
        if (speech[i] > n) {
            continue;
        }
        
        // "speech[i]개의 말이 참이다"라고 말한 횟수를 1 증가
        counts[speech[i]] += 1;
    }

    // 답 구하기
    bool success = false; // 성공여부
    int answer = 0;

    // 가능한 정답이 여러 개인 경우 가장 큰 값을 찾아야 하므로, 
    // n부터 0까지 숫자를 거꾸로 줄여나가며 탐색.
    for (int i = n; i >= 0; i--) {
        // "i개의 말이 참이다"라고 주장한 횟수가 정확히 'i'번이라면, 정답.
        if (i == counts[i]) {
            success = true;
            answer = i;
            break;
        }
    }

    // 출력 처리 -> 정답을 찾았다면 해당 값을 출력
    if (success) {
        cout << answer << "\n";
    } 
    // 모순이면 -1 출력
    else {
        cout << -1 << "\n";
    }

    return 0;
}