package bfs;

import java.io.*;
import java.util.*;

public class BOJ7576 {
    static int N;
    static int M;
    static int[][] graph;
    static int[] dx = {1,-1,0,0};
    static int[] dy = {0,0,1,-1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());

        graph = new int[N][M];
        Queue<int[]> queue = new ArrayDeque<>();

        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j=0; j<M; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
                if (graph[i][j]==1) {
                    queue.offer(new int[] {i,j});
                }
            }
        }

        if (NotExists0()) {
            System.out.println(0);
            return;
        }

        int day = 0;
        while (!queue.isEmpty()) {
            int queueSize = queue.size();
            for (int i=0; i<queueSize; i++) {
                int[] current = queue.poll();
                int curX = current[0];
                int curY = current[1];

                for (int d=0; d<4; d++) {
                    int newX = curX + dx[d];
                    int newY = curY + dy[d];
                    if (0<=newX && newX<N && 0<=newY && newY<M && graph[newX][newY] == 0) {
                        graph[newX][newY] = 1;
                        queue.offer(new int[] {newX, newY});
                    }
                }
            }
            day++;
        }

        if (NotExists0()) {
            System.out.println(day-1);
        } else {
            System.out.println(-1);
        }

    }

    static boolean NotExists0() {
        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                if (graph[i][j]==0) {
                    return false;
                }
            }
        }
        return true;
    }

}
