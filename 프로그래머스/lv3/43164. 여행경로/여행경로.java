import java.util.*;

class Solution {
    int n = 0;
    Map<String, List<String>> adj = new HashMap<>();
	List<String> ans = new ArrayList<>();
    public String[] solution(String[][] t) {
        n = t.length;

        for (int i = 0; i < n; i++) {
            if (!adj.containsKey(t[i][0])) adj.put(t[i][0], new ArrayList<>());
			if (!adj.containsKey(t[i][1])) adj.put(t[i][1], new ArrayList<>());

			List<String> tmp = adj.get(t[i][0]);
			tmp.add(t[i][1]);
            adj.put(t[i][0], tmp);
        }

		for (String key: adj.keySet()) {
			Collections.sort(adj.get(key));
		}


		dfs("ICN");
		Collections.reverse(ans);

        return ans.toArray(new String[0]);
    }

	void dfs(String cur) {
		while (!adj.get(cur).isEmpty()) {
			dfs(adj.get(cur).remove(0));
		}

		if (adj.get(cur).isEmpty()) {
			ans.add(cur);
			return;
		}
	}
}