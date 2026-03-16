#include <iostream>

using namespace std;

int main() {
    // 빠른 입출력을 위한 설정
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // 입력처리
    int a, b, v;
    cin >> a >> b >> v;

    // 달팽이는 정상에서 미끄러지는 범위를 뺀 지점까지(= v-b),
    // 미끄러지면서 등반에 성공하면(= a-b),
    // 미끄러지지 않았을 때 정상에 등반해 있다(= 몫연산)
    int answer = (v - b) / (a - b);

    // 만약 나머지가 있다면 올림해 준다
    if ((v - a) % (a - b)) {
        answer += 1;
    }

    // 출력처리
    cout << answer << "\n";

    return 0;
}