package dfs;

import java.io.*;
import java.util.*;

public class BOJ2573 {

    static int[][] graph;
    static boolean[][] visited;
    static int[][] nearSeaCount;
    static int[] dx = {-1,1,0,0};
    static int[] dy = {0,0,-1,1};
    static int n;
    static int m;
    static boolean is_separated;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        graph = new int[n][m];

        for (int i=0; i<n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j=0; j<m; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int year = 0;
        while (!isAllZero(graph)) {
            InitMelting();
            year++;

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    graph[i][j] -= nearSeaCount[i][j];
                    if (graph[i][j] < 0) graph[i][j] = 0;
                }
            }

            visited = new boolean[n][m];
            is_separated = false;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (!visited[i][j] && graph[i][j] != 0 && !is_separated) {
                        dfs(i, j);
                        is_separated = true;
                    } else if (!visited[i][j] && graph[i][j] != 0 && is_separated) {
                        System.out.println(year);
                        return;
                    }
                }
            }

        }

        System.out.println(0);
    }

    static void dfs(int x, int y) {
        visited[x][y] = true;

        for (int d=0; d<4; d++) {
            int nx = x + dx[d];
            int ny = y + dy[d];
            if (nx >=0 && nx<n && ny>=0 && ny<m && graph[nx][ny] != 0 && !visited[nx][ny]) {
                dfs(nx,ny);
            }
        }
    }

    static boolean isAllZero(int[][] arr) {
        for (int[] row : arr) {
            for (int value : row) {
                if (value!=0) return false;
            }
        }
        return true;
    }

    static void InitMelting() {
        nearSeaCount = new int[n][m];
        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
                if (graph[i][j] != 0) {
                    for (int d = 0; d < 4; d++) {
                        int nearX = i + dx[d];
                        int nearY = j + dy[d];
                        if (nearX >= 0 && nearX < n && nearY >= 0 && nearY < m && graph[nearX][nearY] == 0) {
                            nearSeaCount[i][j]++;
                        }
                    }
                }
            }
        }
    }


}
