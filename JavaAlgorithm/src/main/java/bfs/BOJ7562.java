package bfs;

import java.io.*;
import java.util.*;

public class BOJ7562 {

    static int[][] graph;
    static boolean[][] visited;
    static int goalX;
    static int goalY;
    static int[] dx = {-2,-2,-1,-1,1,1,2,2} ;
    static int[] dy = {-1,1,-2,2,-2,2,-1,1} ;
    static int l;



    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int testcase = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();

        for (int i=0; i<testcase; i++) {
            l = Integer.parseInt(br.readLine());

            graph = new int[l][l];
            visited = new boolean[l][l];

            st = new StringTokenizer(br.readLine());
            int startX = Integer.parseInt(st.nextToken());
            int startY = Integer.parseInt(st.nextToken());

            st = new StringTokenizer(br.readLine());
            goalX = Integer.parseInt(st.nextToken());
            goalY = Integer.parseInt(st.nextToken());

            sb.append(bfs(startX, startY)).append("\n");
        }
        System.out.println(sb);
    }

    static int bfs(int x, int y) {
        int count  = 0;
        Queue<int[]> queue = new ArrayDeque<>();

        queue.offer(new int[]{x,y});
        visited[x][y] = true;

        while (!queue.isEmpty()) {
            int currentLevelSize = queue.size();
            for (int s=0; s<currentLevelSize; s++) {
                int[] current = queue.poll();
                int curX = current[0];
                int curY = current[1];

                if (curX == goalX && curY == goalY) {
                    return count;
                }

                for (int i=0; i<8; i++) {
                    int nx = curX + dx[i];
                    int ny = curY + dy[i];

                    if (0<=nx && nx<l && 0<=ny && ny<l && !visited[nx][ny]) {
                        queue.offer(new int[] {nx,ny});
                        visited[nx][ny] = true;
                    }
                }
            }
            count++;
        }

        return count;
    }

}
