import java.util.*;

class Solution {

	public int[] solution(String today, String[] terms, String[] privacies) {
		List<Integer> ans = new ArrayList<>();
		int todayInDays = convertDateToDays(today, "\\.");

		System.out.println("today : " + todayInDays);

		Map<String, Integer> validUntil = new HashMap<>();

		for (String term: terms) {
			String[] s = term.split(" ");
			validUntil.put(s[0], Integer.parseInt(s[1]));
		}

		for (int i = 0; i < privacies.length; i++) {
			String[] s1 = privacies[i].split(" ");
			int curDay = convertDateToDays(s1[0], "\\.");
			if (curDay + validUntil.get(s1[1]) * 28 <= todayInDays) ans.add(i + 1);

			System.out.println("curDay : " + curDay + ", validDays" + validUntil.get(s1[1]) + " total : " + curDay + validUntil.get(s1[1]));
		}


		return ans.stream().mapToInt(i -> i).toArray();
	}

	private int convertDateToDays(String date, String regex){
		String[] days = date.split(regex);
		return Integer.parseInt(days[0]) * 12 * 28 + Integer.parseInt(days[1]) * 28 + Integer.parseInt(days[2]);
	}
}