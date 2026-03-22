#include <iostream>
#include <vector>

using namespace std;

int main() {
    // N과 M 입력처리
    int n, m;
    cin >> n >> m;

    // 0번부터 N번까지 바구니들
    // 실제로 사용하는 건 1번부터 N번까지 바구니
    vector<int> baskets(n + 1, 0);

    // i, j, k 입력처리
    for (int l = 0; l < m; l++) {
        int i, j, k;
        cin >> i >> j >> k;

        // i번 바구니부터 j번 바구니까지 k번호 공을 넣기
        for (int idx = i; idx <= j; idx++) {
            baskets[idx] = k;
        }
    }

    // 출력처리
    for (int idx = 1; idx <= n; idx++) {
        cout << baskets[idx] << " ";
    }
    cout << "\n";

    return 0;
}