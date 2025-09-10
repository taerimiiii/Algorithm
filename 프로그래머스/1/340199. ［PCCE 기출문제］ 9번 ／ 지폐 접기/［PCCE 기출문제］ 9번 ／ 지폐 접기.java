class Solution {
    public int solution(int[] wallet, int[] bill) {
        int answer = 0;

        int min_wallet;
        int max_wallet;
        if (wallet[0] <= wallet[1]) {
            min_wallet = wallet[0];
            max_wallet = wallet[1];
        }
        else {
            min_wallet = wallet[1];
            max_wallet = wallet[0];
        }
        
        int min_bill;
        int max_bill;
        if (bill[0] <= bill[1]) {
            min_bill = bill[0];
            max_bill = bill[1];
        }
        else {
            min_bill = bill[1];
            max_bill = bill[0];
        }
        
        while (min_bill > min_wallet || max_bill > max_wallet) {
            if (bill[0] > bill[1]) {
                bill[0] /= 2;
                if (bill[0] <= bill[1]) {
                    min_bill = bill[0];
                    max_bill = bill[1];
                }
                else {
                    min_bill = bill[1];
                    max_bill = bill[0];
                }
            }
            else {
                bill[1] /= 2;
                if (bill[0] <= bill[1]) {
                    min_bill = bill[0];
                    max_bill = bill[1];
                }
                else {
                    min_bill = bill[1];
                    max_bill = bill[0];
                }
            }
            answer += 1;
        }
        
        return answer;
    }
}