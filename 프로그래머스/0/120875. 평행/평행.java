class Solution {
    public int solution(int[][] dots) {
        int[] p1 = dots[0];
        int[] p2 = dots[1];
        int[] p3 = dots[2];
        int[] p4 = dots[3];

        if (getSlope(p1, p2) == getSlope(p3, p4)) return 1;
        if (getSlope(p1, p3) == getSlope(p2, p4)) return 1;
        if (getSlope(p1, p4) == getSlope(p2, p3)) return 1;

        return 0;
    }
    
    private double getSlope(int[] dot1, int[] dot2) {
        return (double) (dot2[1] - dot1[1]) / (dot2[0] - dot1[0]);
    }
}