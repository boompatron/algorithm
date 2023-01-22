import javax.swing.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        ArrayList<Float> scoreList = new ArrayList<>();
        int n = Integer.parseInt(br.readLine());
        float m = 0, sum = 0;
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0; i < n; i++) {
            float tmp = Float.parseFloat(st.nextToken());
            scoreList.add(tmp);
            m = Math.max(m, tmp);
        }
        Iterator itr = scoreList.iterator();
        while (itr.hasNext()) sum += (float)itr.next() / m * 100;
        System.out.println(sum / n);
    }
}
