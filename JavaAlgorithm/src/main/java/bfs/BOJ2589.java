package bfs;

import java.io.*;
import java.util.*;

public class BOJ2589 {

    static int L;
    static int M;
    static char[][] graph;
    static boolean[][] visited;
    static int[] dx = {-1,1,0,0};
    static int[] dy = {0,0,-1,1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        L = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        graph = new char[L][M];
        visited = new boolean[L][M];
        for (int i=0; i<L; i++) {
            String line = br.readLine();
            for (int j=0; j<M; j++) {
                graph[i][j] = line.charAt(j);
            }
        }

        int maxTime = 0;
        for (int i=0; i<L; i++) {
            for (int j=0; j<M; j++) {
                if (graph[i][j]=='L') {
                    int bfsTime = bfs(i,j);
                    maxTime = Math.max(maxTime, bfsTime);
                }
            }
        }

        System.out.println(maxTime);

    }

    static int bfs(int x, int y) {
        visited = new boolean[L][M];
        Queue<int[]> queue = new ArrayDeque<>();
        queue.offer(new int[] {x,y});
        visited[x][y] = true;
        int time = 0;

        while (!queue.isEmpty()) {
            int queueSize = queue.size();
            for (int i=0; i<queueSize; i++) {
                int[] current = queue.poll();
                int curX = current[0];
                int curY = current[1];

                for (int d=0; d<4; d++) {
                    int newX = curX + dx[d];
                    int newY = curY + dy[d];

                    if (0<=newX && newX<L && 0<=newY && newY<M && graph[newX][newY]=='L' && !visited[newX][newY]) {
                        queue.offer(new int[] {newX, newY});
                        visited[newX][newY] = true;
                    }
                }

            }
            time++;
        }
        return time-1;
    }

}
