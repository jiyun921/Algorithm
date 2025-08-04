package dfs;

import java.io.*;
import java.util.*;

public class BOJ1926 {
    static int[][] graph;
    static int n;
    static int m;
    static int paintingNum;
    static int paintingArea;
    static final int[] dx = {-1,1,0,0};
    static final int[] dy = {0,0,-1,1};

    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        graph = new int[n][m];

        for (int i=0; i<n; i++) {
            StringTokenizer row = new StringTokenizer(br.readLine());
            for (int j=0; j<m; j++) {
                graph[i][j] = Integer.parseInt(row.nextToken());
            }
        }

        paintingNum = 1;
        int maxArea=0;

        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
                if (graph[i][j]==1) {
                    paintingArea=0;
                    paintingNum++;
                    dfs(i,j);
                    maxArea = Math.max(maxArea, paintingArea);
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        sb.append(paintingNum-1).append("\n");
        sb.append(maxArea);
        System.out.println(sb);

    }

    static void dfs(int x, int y) {
        graph[x][y] = paintingNum;
        paintingArea++;

        for (int i=0; i<4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx>=0 && nx<n && ny>=0 && ny<m && graph[nx][ny]==1) {
                dfs(nx,ny);

            }
        }
    }
}
