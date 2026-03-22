import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.HashMap;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        // 번호로 이름을 찾기 위한 배열 (1번 인덱스부터 사용)
        String[] arr = new String[n + 1];

        // 이름으로 번호를 찾기 위한 맵
        HashMap<String, Integer> name_to_num = new HashMap<>();

        for (int i = 1; i <= n; i++) {
            String name = br.readLine().trim();
            arr[i] = name;               // 인덱스(번호)에 이름 저장
            name_to_num.put(name, i);    // 문자열(이름)을 Key로, 번호를 Value로 저장
        }

        // 검사해야 하는 문제들 입력
        String[] problems = new String[m];
        for (int i = 0; i < m; i++) {
            problems[i] = br.readLine().trim();
        }

        // 답 구하기
        for (int i = 0; i < m; i++) {
            String problem = problems[i];
            
            // 첫 글자가 숫자인지 확인
            if (problem.charAt(0) >= '1' && problem.charAt(0) <= '9') {
                // 입력이 숫자인 경우, 배열에서 인덱스로 바로 접근
                System.out.println(arr[Integer.parseInt(problem)]);
            } else {
                // 입력이 문자인 경우, 맵에서 Key(이름)로 바로 접근
                System.out.println(name_to_num.get(problem));
            }
        }
    }
}