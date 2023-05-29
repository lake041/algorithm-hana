import java.util.*;

class Solution {
    public int solution(int[][] targets) {
        int answer = 0;
        int inter = -1;
        Arrays.sort(targets,(v1,v2)->{
            return v1[1] - v2[1];
        });
        
        for(int[] target : targets){
            if(inter == -1){
                inter = target[1] - 1;
                answer++;
            } 
            if( target[0] <= inter && inter <= target[1]) continue;
            answer++;
            inter = target[1] - 1;
        }
        return answer;
    }
}