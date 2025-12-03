import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());
        int answer = 0;

        if(N!=1){
            PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
            for(int i=1;i<N;i++)
                pq.add(Integer.parseInt(br.readLine()));

            while(pq.peek() >= M){
                int cur = pq.poll();
                cur--;	//가장 큰 후보 투표수 -1
                M++;	//다솜이 투표 수 +1
                answer++;	//매수 횟수 +1
                pq.add(cur);
            }
        }
        bw.write(answer + "");	//매수 횟수 BufferedWriter 저장
        bw.flush();		//결과 출력
        bw.close();
        br.close();
    }
}
