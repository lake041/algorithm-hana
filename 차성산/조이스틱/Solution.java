class Solution {
    public int solution(String name) {
        int answer = 0;
        int move = name.length();
        for(int i = 0 ; i < name.length() ; i++){
            int alphabet = (int) name.charAt(i) - 65;
            int down = alphabet;
            int up = 26 - alphabet;

            answer = answer + Math.min(down, up);
            // System.out.println("Math.min(down, up):" + Math.min(down, up));
            // 연속된 A의 마지막 index
            int continueA =  i + 1;
            // System.out.println("continueA:"+ continueA);
            while(continueA < name.length() && name.charAt(continueA) == 'A'){ 
                    continueA++;
                }
            // 1. 그냥 쭉감
            // 2. 왼쪽으로 먼저 갔다가 오른쪽으로 이동
            // 3. 오른쪽으로 갔다가 왼쪽으로 이동
            move = Math.min(move, 2*i + (name.length() - continueA));
            move = Math.min(move, 2 * (name.length() - continueA) + i);

            // System.out.println("move:" + move);
            }
        answer += move;
         return answer;
        }
    }

