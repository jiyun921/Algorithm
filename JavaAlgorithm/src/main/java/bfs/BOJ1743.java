package bfs;

import java.io.*;
import java.util.*;

public class BOJ1743 {
    static int[][] graph;
    static boolean[][] visited;
    static int[] dx = {1,-1,0,0};
    static int[] dy = {0,0,-1,1};
    static int n;
    static int m;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        graph = new int[n][m];
        visited = new boolean[n][m];

        for (int i=0; i<k; i++) {
            st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken())-1;
            int c = Integer.parseInt(st.nextToken())-1;
            graph[r][c] = 1;

        }

        int MaxArea =  -1;
        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
                if (graph[i][j]==1 && !visited[i][j]) {
                    int trashArea = bfs(i,j);
                    MaxArea = Math.max(MaxArea, trashArea);
                }
            }
        }
        System.out.println(MaxArea);

    }

    static int bfs(int x, int y) {
        int trashArea = 1;
        Queue<int[]> queue = new ArrayDeque<>();

        queue.offer(new int[]{x,y});
        visited[x][y] = true;

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int curX = current[0];
            int curY = current[1];

            for (int i=0; i<4; i++) {
                int nx = curX + dx[i];
                int ny = curY + dy[i];

                if (0<=nx && nx<n && 0<=ny && ny<m && graph[nx][ny]==1 && !visited[nx][ny]) {
                    trashArea++;
                    visited[nx][ny] = true;
                    queue.offer(new int[] {nx,ny});
                }
            }
        }

        return trashArea;

    }
}
