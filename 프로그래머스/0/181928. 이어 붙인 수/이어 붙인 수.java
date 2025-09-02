class Solution {
    public int solution(int[] num_list) {
        int len = num_list.length;
        int pow_even = 1;
        int pow_odd = 1;
        int even = 0;
        int odd = 0;
        for (int i=len-1; i>=0; i--) {
            if (num_list[i] % 2 == 1) {
                odd += num_list[i] * pow_odd;
                pow_odd *= 10;
            }
            else {
                even += num_list[i] * pow_even;
                pow_even *= 10;
            }
        }
            
        int answer = odd + even;
        return answer;
    }
}