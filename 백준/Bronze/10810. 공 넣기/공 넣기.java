import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // N과 M 입력처리
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        // 0번부터 N번까지 바구니들
        // 실제로 사용하는 건 1번부터 N번까지 바구니
        int[] baskets = new int[n + 1];

        // i, j, k 입력처리
        for (int l = 0; l < m; l++) {
            st = new StringTokenizer(br.readLine());
            int i = Integer.parseInt(st.nextToken());
            int j = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());

            // i번 바구니부터 j번 바구니까지 k번호 공을 넣기
            for (int idx = i; idx <= j; idx++) {
                baskets[idx] = k;
            }
        }

        // 출력처리
        StringBuilder sb = new StringBuilder();
        for (int idx = 1; idx <= n; idx++) {
            sb.append(baskets[idx]).append(" ");
        }
        System.out.println(sb.toString());
    }
}