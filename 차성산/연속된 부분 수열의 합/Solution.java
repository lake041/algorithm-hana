class Solution {
    public int[] solution(int[] sequence, int k) {
        int[] answer = new int[2];
        int start = 0;
        int end = 0;
        int min = 1000000;
        int len = sequence.length;
        
        int sum = sequence[0];
        while( (end < len) && (start <= end) ){
        if(sum < k){
            end++;
            if(end < len){
            sum += sequence[end];
            }else break;
        }else if(sum == k){
            if(min > (end - start)){
                min = end - start;
                answer[0] = start; answer[1] = end;
            }
            end++;
            if(end < len){
            sum += sequence[end];
}
        }else{
            sum -= sequence[start];
            start++;
        }
        }
        return answer;
    }
}​