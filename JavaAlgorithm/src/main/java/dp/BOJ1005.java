package dp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ1005 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();;
        int t = Integer.parseInt(br.readLine());

        for (int test=0; test<t; test++) {

            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());

            int[] d = new int[n+1];
            int[] dp = new int[n+1];
            int[] level = new int[n+1];
            int[] maxPrev = new int[n+1];

            List<Integer>[] next_building = new ArrayList[n+1];
            for (int i=1; i<n+1; i++) {
                next_building[i] = new ArrayList<>();
            }

            st = new StringTokenizer(br.readLine());
            for (int i=1; i<n+1; i++) {
                d[i] = Integer.parseInt(st.nextToken());
            }

            int x,y;
            for (int i=0; i<k; i++) {
                st = new StringTokenizer(br.readLine());
                x = Integer.parseInt(st.nextToken());
                y = Integer.parseInt(st.nextToken());
                next_building[x].add(y);
                level[y]+=1;
            }

            int w = Integer.parseInt(br.readLine());

            Queue<Integer> queue = new ArrayDeque<>();

            for (int i=1; i<n+1; i++) {
                if (level[i]==0) {
                    dp[i] = d[i];
                    queue.offer(i);
                }
            }

            while (!queue.isEmpty()) {
                int current = queue.poll();
                for (int next : next_building[current]) {
                    level[next]--;

                    maxPrev[next] = Math.max(maxPrev[next], dp[current]);

                    if (level[next] == 0) {
                        dp[next] = maxPrev[next] + d[next];
                        queue.offer(next);
                    }
                }
            }

            sb.append(dp[w]).append("\n");
        }

        System.out.println(sb);
    }
}
