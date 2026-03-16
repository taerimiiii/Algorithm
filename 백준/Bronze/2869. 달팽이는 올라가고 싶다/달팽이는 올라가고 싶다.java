import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // 입력처리
        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int v = Integer.parseInt(st.nextToken());

        // 달팽이는 정상에서 미끄러지는 범위를 뺀 지점까지(= v-b),
        // 미끄러지면서 등반에 성공하면(= a-b),
        // 미끄러지지 않았을 때 정상에 등반해 있다(= 몫연산)
        int answer = (v - b) / (a - b);

        // 만약 나머지가 있다면 올림해 준다
        if ((v - a) % (a - b) != 0) {
            answer += 1;
        }

        // 출력처리
        System.out.println(answer);
    }
}