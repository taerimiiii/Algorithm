class Solution {
    public int solution(String A, String B) {
        String doubledB = B + B;
        return doubledB.indexOf(A);
    }
}