
class Solution {
	int[] apeachInfo;
	int size, maxScoreDiff = 0;
	int[] ans, wrongAns = {-1};
    public int[] solution(int n, int[] info) {
		apeachInfo = info.clone();
		size = n;

		int[] a = new int[11];
		ans = new int[11];
		for (int i = 0; i < 11; i++) {
			a[i] = 0;
			ans[i] = 0;
		}

		dfs(0, a, n);

        return (maxScoreDiff > 0) ? ans : wrongAns;
    }

	void dfs(int depth, int[] arrows, int leftArrows) {
		if (depth == 11 || leftArrows == 0) {
			arrows[10] += leftArrows;
			int curScoreDiff = calculateScore(arrows);

			if (curScoreDiff > maxScoreDiff || (curScoreDiff == maxScoreDiff && isMoreSmaller(arrows))) {
				maxScoreDiff = curScoreDiff;
				ans = arrows.clone();
			}

			arrows[10] -= leftArrows;
			return;
		}

		dfs(depth + 1, arrows, leftArrows);
		if (leftArrows > apeachInfo[depth]){
			int tmp = apeachInfo[depth] + 1;
			arrows[depth] = tmp;
			dfs(depth + 1, arrows, leftArrows - tmp);
			arrows[depth] = 0;
		}
	}

	int calculateScore(int[] ryan) {
		int score = 0;
        // int ryanScore = 0, apeachScore = 0;
		for (int i = 0; i < 11; i++) {
			if (ryan[i] == 0 && apeachInfo[i] == 0) continue;
            score += (ryan[i] > apeachInfo[i]) ? 10 - i : i - 10;
			// if (ryan[i] > apeachInfo[i]) 	ryanScore += 10 - i;
			// else 							apeachScore += 10 - i;
		}
		return score;
	}

	boolean isMoreSmaller(int[] ryan) {
		for (int i = 10; i > -1; i--) {
			if (ryan[i] == 0 && ans[i] == 0) continue;
			return ryan[i] > ans[i];
		}

		return true;
	}
}