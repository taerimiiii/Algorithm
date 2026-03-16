import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 전투의 개수 T 입력처리
        int t = Integer.parseInt(br.readLine());

        // 반복문을 이용하여 전투를 T번 치른다.
        // 출력 용이성을 위해, battel_num에 1부터 t까지 수를 넣으며 반복한다.
        for (int battel_num = 1; battel_num <= t; battel_num++) {
            
            // 간달프 군대에 참여한 종족 수를 list(배열)로 입력받는다.
            String[] gandalfInput = br.readLine().split(" ");
            int[] gandalf = Arrays.stream(gandalfInput).mapToInt(Integer::parseInt).toArray();
            
            // 사우론 군대에 참여한 종족 수를 list(배열)로 입력받는다.
            String[] sauronInput = br.readLine().split(" ");
            int[] sauron = Arrays.stream(sauronInput).mapToInt(Integer::parseInt).toArray();

            // 간달프 군대의 점수 합을 구한다
            // 간달프 군대 : 호빗1, 인간2, 엘프3, 드워프3, 독수리4, 마법사10
            int sum_gandalf = gandalf[0] + gandalf[1]*2 + gandalf[2]*3 + gandalf[3]*3 + gandalf[4]*4 + gandalf[5]*10;
            
            // 사우론 군대의 점수 합을 구한다.
            // 사우론 군대 : 오크1, 인간2, 워그2, 고블린2, 우럭하이3, 트롤5, 마법사10
            int sum_sauron = sauron[0] + sauron[1]*2 + sauron[2]*2 + sauron[3]*2 + sauron[4]*3 + sauron[5]*5 + sauron[6]*10;
            
            // 조건문을 통해 승리한 군대에 따라 결과를 출력한다.
            if (sum_gandalf > sum_sauron) {
                System.out.println("Battle " + battel_num + ": Good triumphs over Evil");
            } else if (sum_gandalf < sum_sauron) {
                System.out.println("Battle " + battel_num + ": Evil eradicates all trace of Good");
            } else {
                System.out.println("Battle " + battel_num + ": No victor on this battle field");
            }
        }
    }
}