import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // 다솜의 방 번호(N)를 문자열로 입력 받습니다.
        String n = br.readLine().trim();

        // 0~9 숫자의 개수를 저장할 배열을 선언합니다.
        int[] nums_count = new int[10];

        // 다솜의 방 번호를 처음부터 끝까지 순회하며 필요한 숫자 개수를 저장합니다.
        for (char num : n.toCharArray()) {
            nums_count[num - '0'] += 1;
        }

        // 6과 9는 뒤집어서 사용할 수 있는 것을 처리합니다.
        // 예시1) 6과 9가 합쳐서 총 5개 필요하다면 3세트가 필요합니다.
        // 예시2) 6과 9가 합쳐서 총 6개 필요하다면 3세트가 필요합니다.

        // 정수 나눗셈(/)은 나머지를 버리기 때문에, 
        // 총 필요한 6과 9개수에 1을 더하고 2로 나누어 주면, 
        // 최소한으로 필요한 세트를 구할 수 있습니다.
        int temp = (nums_count[6] + nums_count[9] + 1) / 2;
        nums_count[6] = temp;
        nums_count[9] = temp;

        // 필요한 세트의 개수의 최솟값(배열의 최댓값)을 구합니다.
        int max_count = 0;
        for (int count : nums_count) {
            if (count > max_count) {
                max_count = count;
            }
        }

        // 출력처리
        System.out.println(max_count);
    }
}