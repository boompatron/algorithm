import java.util.HashSet;
import java.util.Set;

class Solution {
	public int solution(int[] nums) {
		Set<Integer> s = new HashSet<>();
		for (int num: nums){
			s.add(num);
		}

		return Math.min(nums.length / 2, s.size());
	}
}