package bfs;

import java.io.*;
import java.util.*;

public class BOJ7576 {
    static int N;
    static int M;
    static int[][] graph;
    static boolean[][] visited;
    static int[] dx = {1,-1,0,0};
    static int[] dy = {0,0,1,-1};
    static boolean check;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());

        graph = new int[N][M];
        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j=0; j<M; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        if (!exists0()) {
            System.out.println(0);
            return;
        }

        int day = 0;
        while (exists0()) {
            visited = new boolean[N][M];
            check = false;
            for (int i=0; i<N; i++) {
                for (int j=0; j<M; j++) {
                    if (graph[i][j]==1 && !visited[i][j]) {
                        bfs(i,j);
                    }
                }
            }
            if (!check) {
                System.out.println(-1);
                return;
            }
            day++;
        }
        System.out.println(day);
    }

    static boolean exists0() {
        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                if (graph[i][j]==0) {
                    return true;
                }
            }
        }
        return false;
    }

    static void bfs(int x, int y) {
        for (int i=0; i<4; i++) {
            int newX = x + dx[i];
            int newY = y + dy[i];
            if (0<=newX && newX<N && 0<=newY && newY<M && graph[newX][newY] == 0) {
                graph[newX][newY] = 1;
                visited[newX][newY] = true;
                check = true;
            }
        }
    }

}
