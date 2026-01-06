package dp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ9655 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        boolean[] dp = new boolean[n+1];
        if (n>=1) {
            dp[1] = true;
        }
        if (n>=2) {
            dp[2] = false;
        }
        if (n>=3) {
            dp[3] = true;
        }

        for (int i=4; i<n+1; i++) {
            dp[i] = !dp[i-1] || !dp[i-3];
        }

        System.out.println(dp[n] ? "SK" : "CY");
    }
}
