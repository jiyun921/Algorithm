package bfs;

import java.io.*;
import java.util.*;

public class BOJ21736 {

    static char[][] graph;
    static boolean[][] visited;
    static int[] dx = {1,-1,0,0};
    static int[] dy = {0,0,1,-1};
    static int n;
    static int m;
    static int count;

    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        graph = new char[n][m];
        visited = new boolean[n][m];

        int Ix=0;
        int Iy=0;

        for (int i=0; i<n; i++){
            String line = br.readLine();
            for (int j=0; j<m; j++) {
               graph[i][j] = line.charAt(j);
               if (graph[i][j]=='I') {
                   Ix = i;
                   Iy = j;
               }
            }
        }

        int result = bfs(Ix,Iy);
        System.out.println(result==0 ? "TT" : result);

    }

    static int bfs(int x, int y) {
         Queue<int[]> queue = new ArrayDeque<>();

         queue.offer(new int[]{x,y});
         visited[x][y] = true;

         while (!queue.isEmpty()) {
             int[] current = queue.poll();
             int currentX = current[0];
             int currentY = current[1];

             for (int i=0; i<4; i++) {
                 int nx = currentX + dx[i];
                 int ny = currentY + dy[i];

                 if (0<=nx && nx<n && 0<=ny && ny<m && graph[nx][ny] != 'X' && !visited[nx][ny]) {
                     queue.offer(new int[]{nx,ny});
                     visited[nx][ny] = true;
                     if (graph[nx][ny]=='P') {
                         count++;
                     }
                 }
             }
         }
         return count;


    }
}
