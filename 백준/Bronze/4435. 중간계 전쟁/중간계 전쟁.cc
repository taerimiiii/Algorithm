#include <iostream>
#include <vector>

using namespace std;

int main() {
    // 전투의 개수 T 입력처리
    int t;
    cin >> t;

    // 반복문을 이용하여 전투를 T번 치른다.
    // 출력 용이성을 위해, battel_num에 1부터 t까지 수를 넣으며 반복한다.
    for (int battel_num = 1; battel_num <= t; battel_num++) {
        
        // 간달프 군대에 참여한 종족 수를 list(vector)로 입력받는다.
        vector<int> gandalf(6);
        for (int i = 0; i < 6; i++) {
            cin >> gandalf[i];
        }
        
        // 사우론 군대에 참여한 종족 수를 list(vector)로 입력받는다.
        vector<int> sauron(7);
        for (int i = 0; i < 7; i++) {
            cin >> sauron[i];
        }

        // 간달프 군대의 점수 합을 구한다
        // 간달프 군대 : 호빗1, 인간2, 엘프3, 드워프3, 독수리4, 마법사10
        int sum_gandalf = gandalf[0] + gandalf[1]*2 + gandalf[2]*3 + gandalf[3]*3 + gandalf[4]*4 + gandalf[5]*10;
        
        // 사우론 군대의 점수 합을 구한다.
        // 사우론 군대 : 오크1, 인간2, 워그2, 고블린2, 우럭하이3, 트롤5, 마법사10
        int sum_sauron = sauron[0] + sauron[1]*2 + sauron[2]*2 + sauron[3]*2 + sauron[4]*3 + sauron[5]*5 + sauron[6]*10;
        
        // 조건문을 통해 승리한 군대에 따라 결과를 출력한다.
        if (sum_gandalf > sum_sauron) {
            cout << "Battle " << battel_num << ": Good triumphs over Evil" << endl;
        } else if (sum_gandalf < sum_sauron) {
            cout << "Battle " << battel_num << ": Evil eradicates all trace of Good" << endl;
        } else {
            cout << "Battle " << battel_num << ": No victor on this battle field" << endl;
        }
    }

    return 0;
}