#include <iostream>

using namespace std;

int main() {
    // 입력 처리
    int n;
    cin >> n;

    int answer = 0; // 답을 저장하는 변수
    int time = 30;  // 남은 시간

    for (int i = 0; i < n; i++) {
        int chap;
        cin >> chap;

        // 공부하는데 걸리는 시간이 남은 시간보다 작거나 같을 경우
        // 성공적으로 공부하므로 답+1
        if (chap <= time) {
            time -= chap;
            answer += 1;
        }
        // 공부할 게 남았지만 덮어버리는 경우
        else {
            // 챕터의 절반이 시간 안에 공부한 양을 넘을 경우
            // 잘 기억했으므로 답+1
            if (chap / 2 >= (chap - time)) {
                answer += 1;
            }
            time = 0;
        }

        // 남은 시간이 0 이라면 30분 휴식을 취하고, 다시 시간이 30분으로 늘어남.
        if (time == 0) {
            time = 30;
        }
    }

    cout << answer << endl;

    return 0;
}