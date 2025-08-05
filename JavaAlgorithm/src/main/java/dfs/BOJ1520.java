package dfs;

import java.io.*;
import java.util.*;

public class BOJ1520 {
    static int[][] graph;
    static boolean[][] visited;
    static int[] dx = {1,-1,0,0};
    static int[] dy = {0,0,-1,1};
    static int m,n;
    static int count;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        m  = Integer.parseInt(st.nextToken());
        n  = Integer.parseInt(st.nextToken());
        graph = new int[m][n];
        visited = new boolean[m][n];

        for (int i=0; i<m ; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j=0; j<n; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        dfs(0,0);
        System.out.println(count);

    }

    static void dfs(int x, int y) {
        if (x==m-1 && y==n-1) {
            count++;
            return;
        }

        visited[x][y] = true;
        for (int i=0; i<4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx>=0 && nx<m && ny>=0 && ny<n && !visited[nx][ny] && graph[nx][ny] < graph[x][y]) {
                dfs(nx,ny);
            }
        }

        visited[x][y] = false;
    }
}
