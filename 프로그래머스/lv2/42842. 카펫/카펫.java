class Solution {
    private static int[] ans = new int[2];
    public int[] solution(int brown, int yellow) {
        int s = brown + yellow;
        for(int n = 1; n <= s; n++){
            if(s % n == 0){
                int m = s / n;
                if ((n - 2) * (m - 2) == yellow){
                    System.out.println(m + ", " + n);
                    ans[0] = m;
                    ans[1] = n;
                    break;
                }
            }
        }
        return ans;
    }
}