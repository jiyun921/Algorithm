package dp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ2565 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int cnt = Integer.parseInt(br.readLine());
        StringTokenizer st;
        int[][] line = new int[cnt][2];
        int[] dp = new int[cnt];

        for (int i=0; i<cnt; i++) {
            st = new StringTokenizer(br.readLine());
            line[i][0] =Integer.parseInt(st.nextToken());
            line[i][1] =Integer.parseInt(st.nextToken());
        }

        Arrays.sort(line, (x,y) -> x[0]-y[0]);

        dp[0] = 1;
        for (int i=1; i<cnt; i++) {
            int prev_dp_max = 0;
            for (int j=0; j<i; j++) {
                if (line[i][1] > line[j][1] && prev_dp_max <dp[j]) {
                    prev_dp_max = dp[j];
                }
            }
            dp[i] = prev_dp_max +1;
        }

        int dp_max = dp[0];
        for (int i=0; i<cnt; i++) {
            if (dp_max<dp[i]) {
                dp_max = dp[i];
            }
        }

        System.out.println(cnt-dp_max);
    }
}
