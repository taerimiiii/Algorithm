import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.HashMap;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // n과 m 한 줄 공백 입력 처리
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        // 해시맵 자료형을 이용한 집합S 입력 처리
        HashMap<String, Boolean> s_set = new HashMap<>();
        for (int i = 0; i < n; i++) {
            String k = br.readLine().trim();
            s_set.put(k, true);     // 문자열을 key로 두고 value를 True로 준다.
        }

        // 정답을 저장할 변수 선언
        int answer = 0;

        // 답 구하기
        for (int i = 0; i < m; i++) {
            String target = br.readLine().trim(); // 검사해야 하는 문자열 입력
            if (s_set.containsKey(target)) {      // 타겟 문자열이 S집합에 있다면
                answer += 1;                      // 답+1
            }
        }

        // 출력처리
        System.out.println(answer);
    }
}