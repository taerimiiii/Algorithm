import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 입력 처리
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();
        int r = sc.nextInt();

        int[][] arr = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                arr[i][j] = sc.nextInt();
            }
        }

        for (int i = 0; i < r; i++) {
            int cal = sc.nextInt();

            if (cal == 1) {
                for (int j = 0; j < n/2; j++) {
                    int[] temp = arr[j];
                    arr[j] = arr[n - 1 - j];
                    arr[n - 1 - j] = temp;
                }
            }
            else if (cal == 2) {
                for (int j = 0; j < n; j++) {
                    for (int k = 0; k < m / 2; k++) {
                        int temp = arr[j][k];
                        arr[j][k] = arr[j][m - 1 - k];
                        arr[j][m - 1 - k] = temp;
                    }
                }
            }
            else if (cal == 3) {
                int[][] temp = new int[m][n];
                for (int j = 0; j < n; j++) {
                    for (int k = 0; k < m; k++) {
                        temp[k][n - 1 - j] = arr[j][k];
                    }
                }
                arr = temp;

                int n_temp = n;
                n = m;
                m = n_temp;
            }
            else if (cal == 4) {
                int[][] temp = new int[m][n];
                for (int j = 0; j < n; j++) {
                    for (int k = 0; k < m; k++) {
                        temp[m - 1 - k][j] = arr[j][k];
                    }
                }
                arr = temp;

                int n_temp = n;
                n = m;
                m = n_temp;
            }
            else if (cal == 5) {
                int[][] temp = new int[n][m];
                for (int j = 0; j < n/2; j++) {
                    for (int k = 0; k < m/2; k++) {
                        temp[j][k + m/2] = arr[j][k];
                        temp[j + n/2][k + m/2] = arr[j][k + m/2];
                        temp[j + n/2][k] = arr[j + n/2][k + m/2];
                        temp[j][k] = arr[j + n/2][k];
                    }
                }
                arr = temp;
            } 
            else {
                int[][] temp = new int[n][m];
                for (int j = 0; j < n/2; j++) {
                    for (int k = 0; k < m/2; k++) {
                        temp[j + n/2][k] = arr[j][k];
                        temp[j + n/2][k + m/2] = arr[j + n/2][k];
                        temp[j][k + m/2] = arr[j + n/2][k + m/2];
                        temp[j][k] = arr[j][k + m/2];
                    }
                }
                arr = temp;
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
        
        sc.close();
    }
}
