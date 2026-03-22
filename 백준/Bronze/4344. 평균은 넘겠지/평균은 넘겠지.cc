#include <iostream>
#include <vector>
#include <iomanip> // 소수점 출력을 위한 헤더

using namespace std;

int main() {
    // C 입력처리
    int c;
    cin >> c;

    for (int t = 0; t < c; t++) {
        // 학생수와 학생들의 점수 입력처리
        int student_num;
        cin >> student_num;
        vector<int> scores(student_num);
        
        // 학생들 점수 전체 합 구하기
        double sum = 0;
        for (int i = 0; i < student_num; i++) {
            cin >> scores[i];
            sum += scores[i];
        }

        // 평균 구하기
        double average = sum / student_num;

        // 평균을 넘는 학생 수 구하기
        int student_count = 0;
        for (int i = 0; i < student_num; i++) {
            if (scores[i] > average) {
                student_count += 1;
            }
        }
        
        // 평균을 넘는 학생들의 비율 구하기
        double rate = (double) student_count / student_num * 100;

        // 구한 비율을 반올림하여 소수점 셋째자리까지 출력
        cout << fixed << setprecision(3) << rate << "%\n";
    }

    return 0;
}