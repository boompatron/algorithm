import java.util.*;

class Solution {
	static int n = 0;

	public int[] solution(String[] genres, int[] plays) {
		n = genres.length;

		Map<String, PriorityQueue<Song>> map = new HashMap<>();
		PriorityQueue<Genre> totalPlays = new PriorityQueue<>();
		Map<String, Integer> sortedByGenre = new HashMap<>();

		for (int i = 0; i < n; i++) {
			sortedByGenre.put(genres[i], sortedByGenre.getOrDefault(genres[i], 0) + plays[i]);
			if (!map.containsKey(genres[i])) {
				map.put(genres[i], new PriorityQueue<>());
			}
			map.get(genres[i]).add(new Song(i, plays[i]));
		}

		for (String key : sortedByGenre.keySet()) {
			totalPlays.add(new Genre(key, sortedByGenre.get(key)));
		}

		// for (String key: map.keySet()){
		// 	System.out.println(key);
		// 	while (!map.get(key).isEmpty()) {
		// 		Song cur = map.get(key).poll();
		// 		System.out.println(cur.num + ", " + cur.plays);
		// 	}
		// }
		//
		// while (!totalPlays.isEmpty()) {
		// 	Genre g = totalPlays.poll();
		// 	System.out.println(g.name + ", " + g.total);
		// }

		List<Integer> ans = new ArrayList<>();

		while (!totalPlays.isEmpty()) {
			Genre cur = totalPlays.poll();
			int size = Math.min(2, map.get(cur.name).size());
			System.out.println(cur.name + ", " + size);
			for (int i = 0; i < size; i++) {
				Song song = map.get(cur.name).poll();
				ans.add(song.num);
			}
		}
		return ans.stream().mapToInt(i -> i).toArray();
	}

	static class Song implements Comparable<Song> {
		int num;
		int plays;

		public Song(int num, int plays) {
			this.num = num;
			this.plays = plays;
		}

		@Override
		public int compareTo(Song target) {
			if (this.plays != target.plays)
				return this.plays < target.plays ? 1 : -1;
			else
				return this.num >= target.num ? 1 : -1;
		}
	}

	static class Genre implements Comparable<Genre> {
		String name;
		int total;

		public Genre(String name, int total) {
			this.name = name;
			this.total = total;
		}

		@Override
		public int compareTo(Genre target) {
			return this.total <= target.total ? 1 : -1;
		}
	}
}