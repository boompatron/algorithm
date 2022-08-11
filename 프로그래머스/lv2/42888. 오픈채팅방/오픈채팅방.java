import java.util.HashMap;
import java.util.LinkedList;

class Solution {
    public String[] solution(String[] record) {
        HashMap<String, String> map = new HashMap<>();
        LinkedList<Pair> log = new LinkedList<>();
        for(String r : record){
            String[] tmp = r.split(" ");
            if(tmp[0].equals("Enter")) {
                map.put(tmp[1], tmp[2]);
                log.add(new Pair(true, tmp[1]));
            }
            else if(tmp[0].equals("Change")) {
                map.put(tmp[1], tmp[2]);
            }
            else{
                log.add(new Pair(false, tmp[1]));
            }
        }
        String[] answer = new String[log.size()];
        int i = 0;
        for(Pair p : log){
            if(p.isEnter)
                answer[i++] = (map.get(p.uid) + "님이 들어왔습니다.");
            else
                answer[i++] = (map.get(p.uid) + "님이 나갔습니다.");
        }
        return answer;
    }
}
class Pair{
    boolean isEnter;
    String uid;
    public Pair(boolean isEnter, String uid){
        this.isEnter = isEnter;
        this.uid = uid;
    }
}