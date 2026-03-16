import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // Math.abs() 함수:
        // 소괄호 안의 값의 절대값(=거리)을 구하는 함수

        // 입력처리
        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(br.readLine());

        // distance : 첫번째 혹은 두번째 버튼만을 눌러서 B에 도착하는 횟수
        // 초기값은 A와 B 사이 거리
        int distance = Math.abs(a - b);

        // success : 즐겨찾기 버튼 이용 여부를 저장하는 변수
        // 초기값은 사용X (False)
        boolean success = false;

        for (int i = 0; i < n; i++) {

            // 즐겨찾기 버튼 입력 처리
            int button = Integer.parseInt(br.readLine());

            // 만약 즐겨찾기 버튼과 B사이 거리가 A와 B사이 거리보다 가깝다면,
            if (Math.abs(button - b) < distance) {
                distance = Math.abs(button - b);  // distance 갱신
                success = true;                   // 즐겨찾기 버튼 사용O
            }
        }

        // 출력 처리
        if (success) {             // 만약 즐겨찾기 버튼을 이용해야 한다면,
            System.out.println(1 + distance);  // 즐겨찾기 버튼 누르기(1회) + 첫 번째 혹은 두 번째 버튼을 눌러서 B에 도착(distance회)
        } else {                   // 만약 즐겨찾기 버튼을 이용하지 않는다면,
            System.out.println(distance);      // 첫 번째 혹은 두 번째 버튼만을 눌러서 B에 도착(distance회)
        }
    }
}