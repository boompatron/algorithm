import java.util.*;

class Solution {

	private static int n, emticonSize;
	private static int ansPrice = 0;
	private static int ansSubscribe = 0;
	private static final int[] discountAmount = {10, 20, 30, 40};// {0.1, 0.2, 0.3, 0.4};
	private static int[][] u;
	private static int[] e;

	public int[] solution(int[][] users, int[] emoticons) {
		n = users.length;
		emticonSize = emoticons.length;
		u = users;
		e = emoticons;

		dfs(new ArrayList<>());

		int[] ans = new int[2];
        ans[0] = ansSubscribe;
        ans[1] = ansPrice;
		return ans;
	}

	private void dfs(List<Integer> discountRates){
		if (discountRates.size() == emticonSize) {
			int tmpTotalPrice = 0, tmpSubNum = 0;

			for (int[] user: u) {
				int amount = 0;
				for (int i = 0; i < emticonSize; i++){
					if (discountRates.get(i) >= user[0]){
						amount += (int)((100 - discountRates.get(i)) * e[i] / 100);
					}
				}
				if (amount >= user[1]) {
					tmpSubNum++;
				} else {
					tmpTotalPrice += amount;
				}
			}

			if (ansSubscribe < tmpSubNum || (ansSubscribe == tmpSubNum && ansPrice < tmpTotalPrice)) {
				ansPrice = tmpTotalPrice;
				ansSubscribe = tmpSubNum;
			}
			return;
		}

		for (int da: discountAmount){
			discountRates.add(da);
			dfs(discountRates);
			discountRates.remove(discountRates.size() - 1);
		}
	}
}