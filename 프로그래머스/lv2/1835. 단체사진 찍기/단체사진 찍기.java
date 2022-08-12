class Solution{
    private static String[] Friends = {"A", "C", "F", "J", "M", "N", "R", "T"};
    private int ans = 0;
    public int solution(int n, String[] data){
        boolean[] isVisited = new boolean[8];
        DFS("", isVisited, data);
        return ans;
    }
    private void DFS(String order, boolean[] isVisited ,String[] datas){
        if(order.length() == 8){
            if(check(order, datas)){
                ans++;
            }
            return;
        }
        for(int i = 0; i < 8; i++){
            if(!isVisited[i]){
                isVisited[i] = true;
                String o = order + Friends[i];
                DFS(o, isVisited, datas);
                isVisited[i] = false;
            }
        }
    }
    private boolean check(String order, String[] datas){
        for(String d : datas){
            int pos1 = order.indexOf(d.charAt(0));
            int pos2 = order.indexOf(d.charAt(2));
            char operation = d.charAt(3);
            int diff = d.charAt(4) - '0' + 1;
            if(operation == '=')        {if(!(Math.abs(pos1 - pos2) == diff)) return false;}
            else if(operation == '>')   {if(!(Math.abs(pos1 - pos2) >  diff)) return false;}
            else if(operation == '<')   {if(!(Math.abs(pos1 - pos2) <  diff)) return false;}
        }
        return true;
    }
}