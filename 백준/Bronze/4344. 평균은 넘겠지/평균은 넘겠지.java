import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // C 입력처리
        int c = Integer.parseInt(br.readLine().trim());

        for (int t = 0; t < c; t++) {
            // 학생수와 학생들의 점수 입력처리
            StringTokenizer st = new StringTokenizer(br.readLine());
            int student_num = Integer.parseInt(st.nextToken());
            int[] scores = new int[student_num];

            // 학생들의 점수 전체 합 구하기
            double sum_score = 0;
            for (int i = 0; i < student_num; i++) {
                scores[i] = Integer.parseInt(st.nextToken());
                sum_score += scores[i];
            }

            // 평균 구하기
            double average = sum_score / student_num;

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
            System.out.printf("%.3f%%\n", rate);
        }
    }
}