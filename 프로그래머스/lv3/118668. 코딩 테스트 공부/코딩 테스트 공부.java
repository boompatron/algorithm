class Solution {

	int targetAl = 0;
	int targetCo = 0;
    public int solution(int alp, int cop, int[][] problems) {
        int answer = 0;

		for (int[] problem: problems){
			targetAl = Math.max(targetAl, problem[0]);
			targetCo = Math.max(targetCo, problem[1]);
		}

		int[][] dp = new int[targetAl + 1][targetCo + 1];
        
        for (int i = 0; i < targetAl + 1; i++) {
			for (int j = 0; j < targetCo + 1; j++) {
				dp[i][j] = 10000000;
			}
		}

		alp = Math.min(alp, targetAl);
		cop = Math.min(cop, targetCo);

		dp[alp][cop] = 0;

		for (int i = alp; i < targetAl + 1; i++) {
			for (int j = cop; j < targetCo + 1; j++) {

				if (i < targetAl) dp[i + 1][j] = Math.min(dp[i + 1][j], dp[i][j] + 1);
				if (j < targetCo) dp[i][j + 1] = Math.min(dp[i][j + 1], dp[i][j] + 1);

				for (int[] problem: problems) {
					if (i >= problem[0] && j >= problem[1]){
						int tmpI = Math.min(targetAl, i + problem[2]);
						int tmpJ = Math.min(targetCo, j + problem[3]);

						dp[tmpI][tmpJ] = Math.min(dp[tmpI][tmpJ], dp[i][j] + problem[4]);
					}
				}
			}
		}

        return dp[targetAl][targetCo];
    }
}