class Solution {
    public String solution(String my_string, int[][] queries) {
        for (int i = 0; i < queries.length; i++) {
            int s = queries[i][0];
            int e = queries[i][1];
            
            String prefix = my_string.substring(0, s);
            String middle = my_string.substring(s, e + 1);
            String suffix = my_string.substring(e + 1);
            
            String reversedMiddle = new StringBuilder(middle).reverse().toString();
            
            my_string = prefix + reversedMiddle + suffix;
        }
        
        return my_string;
    }
}