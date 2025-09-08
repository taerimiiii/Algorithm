class Solution {
    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) {
        String answer = "";
        int video_mmss, pos_mmss, op_start_mmss, op_end_mmss, commands_len;
        
        video_mmss = (video_len.charAt(0) - '0') * 1000 + (video_len.charAt(1) - '0') * 100
            + (video_len.charAt(3) - '0') * 10 + (video_len.charAt(4) - '0');
        pos_mmss = (pos.charAt(0) - '0') * 1000 + (pos.charAt(1) - '0') * 100
            + (pos.charAt(3) - '0') * 10 + (pos.charAt(4) - '0');
        op_start_mmss = (op_start.charAt(0) - '0') * 1000 + (op_start.charAt(1) - '0') * 100
            + (op_start.charAt(3) - '0') * 10 + (op_start.charAt(4) - '0');
        op_end_mmss = (op_end.charAt(0) - '0') * 1000 + (op_end.charAt(1) - '0') * 100 + 
            (op_end.charAt(3) - '0') * 10 + (op_end.charAt(4) - '0');

        if (op_start_mmss <= pos_mmss && pos_mmss <= op_end_mmss) {
            pos_mmss = op_end_mmss;
        }

        commands_len = commands.length;
        for (int i=0; i<commands_len; i++) {
            if (commands[i].equals("next")) {
                pos_mmss += 10;
                if (pos_mmss % 100 >= 60) {
                    pos_mmss = pos_mmss + 100 - 60;
                }
                if (pos_mmss > video_mmss) {
                    pos_mmss = video_mmss;
                }
                if (op_start_mmss <= pos_mmss && pos_mmss <= op_end_mmss) {
                    pos_mmss = op_end_mmss;
                }
            }
            if (commands[i].equals("prev")) {
                if (pos_mmss <= 10) {
                    pos_mmss = 0;
                }
                else if (pos_mmss % 100 < 10) {
                    pos_mmss = pos_mmss - 100 + 50;
                }
                else {
                    pos_mmss -= 10;
                }
                
                if (op_start_mmss <= pos_mmss && pos_mmss <= op_end_mmss) {
                    pos_mmss = op_end_mmss;
                }
            }
        }
        
        int pos_mm, pos_ss;
        pos_mm = pos_mmss / 100;
        pos_ss = pos_mmss % 100;
        
        if (pos_mm < 10) {
            answer = "0" + pos_mm;
        }
        else {
            answer = "" + pos_mm;
        }
        
        answer += ":";
        
        if (pos_ss < 10) {
            answer += "0" + pos_ss;
        }
        else {
            answer += "" + pos_ss;
        }
        return answer;
    }
}