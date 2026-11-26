import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder output = new StringBuilder();
        
        while (true) {
            String line = br.readLine();
            
            if (line.equals("END")) {
                break;
            }
            
            String reversed = new StringBuilder(line).reverse().toString();
            output.append(reversed).append("\n");
        }
        
        System.out.print(output);
    }
}