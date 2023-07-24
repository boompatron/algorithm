import java.util.*;

class Solution {
	int n = 0;
	int m = 0;
	Map<String, List<String>> adj = new HashMap<>();
	Deque<A> dq = new LinkedList<>();
	Set<String> visited = new HashSet<>();

	public int solution(String begin, String target, String[] words) {
		n = words.length;
		m = begin.length();

		adj.put(begin, new ArrayList<>());
        for (int i = 0; i < n; i++) adj.put(words[i], new ArrayList<>());
        
		visited.add(begin);
		for (int i = 0; i < n; i++) {
			int cnt = 0;
			for (int k = 0; k < m; k++) {
				if (begin.charAt(k) != words[i].charAt(k))
					cnt++;
			}
			if (cnt == 1) adj.get(begin).add(words[i]);
		}

        boolean isTargetInWords = false;
        
		for (int i = 0; i < n; i++) {
			String cur = words[i];
            
            if (cur.equals(target)) isTargetInWords = true;
            
			// adj.put(cur, new ArrayList<>());
			for (int j = i + 1; j < n; j++) {
				int cnt = 0;
				for (int k = 0; k < m; k++) {
					if (cur.charAt(k) != words[j].charAt(k))
						cnt++;
				}

				if (cnt == 1) {
                    adj.get(cur).add(words[j]);
                    adj.get(words[j]).add(cur);
                }
                
			}
		}
        
        if (!isTargetInWords) return 0;

		dq.add(new A(begin, 0));
		while (!dq.isEmpty()) {
			A a = dq.poll();
			if (a.word.equals(target)) return a.distance;

			for (String aa: adj.get(a.word)) {
				if (!visited.contains(aa)) {
					dq.add(new A(aa, a.distance + 1));
				}
			}
		}

		return 0;
	}
}

class A {
	String word;
	int distance;

	public A( String word, int distance) {
		this.distance = distance;
		this.word = word;
	}
}