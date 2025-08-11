package bfs;

import java.io.*;
import java.util.*;

public class BOJ11449 {
    static boolean[][] visited;
    static int[] dx = {1,-1,0,0};
    static int[] dy = {0,0,-1,1};
    static List<int[]> remove;
    static List<int[]> remove_candidate;
    static int n=12;
    static int m=6;
    static char[][] graph = new char[n][m];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int i=0; i<n; i++) {
            String line = br.readLine();
            for (int j=0; j<m; j++) {
                graph [i][j] = line.charAt(j);
            }
        }

        int chain=0;
        while(true) {
            boolean hasDelete=false;
            visited = new boolean[n][m];
            remove = new ArrayList<>();
            for (int i=0; i<n; i++) {
                for (int j=0; j<m; j++) {
                    if (graph[i][j] != '.' && !visited[i][j]) {
                        int count = bfs(i,j,graph[i][j]);
                        if (count>=4) {
                            for (int[] pair : remove_candidate) {
                                remove.add(Arrays.copyOf(pair, pair.length));
                            }
                            hasDelete = true;
                        }
                    }
                }
            }

            if (!hasDelete) break;

            for (int[] pair : remove) {
                graph[pair[0]][pair[1]] = '.';
            }

            for (int y=0; y<m; y++) {
                int writeX = n-1;
                for (int x = writeX; x>=0; x--) {
                    if (graph[x][y]!='.') {
                        char c = graph[x][y];
                        graph[x][y] = '.';
                        graph[writeX][y] = c;
                        writeX--;
                    }
                }
            }
            chain++;
        }

        System.out.println(chain);
    }

    static int bfs(int x, int y, char color) {
        int count = 1;
        Queue<int[]> queue = new ArrayDeque<>();
        remove_candidate = new ArrayList<>();

        queue.offer(new int[] {x,y});
        remove_candidate.add(new int[] {x,y});
        visited[x][y] = true;

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int currentX = current[0];
            int currentY = current[1];

            for (int i=0; i<4; i++) {
                int nx = currentX + dx[i];
                int ny = currentY + dy[i];

                if (0<=nx && nx<n && 0<=ny && ny<m && graph[nx][ny] == color && !visited[nx][ny]) {
                    queue.offer(new int[]{nx,ny});
                    remove_candidate.add(new int[] {nx,ny});
                    visited[nx][ny] = true;
                    count++;
                }
            }
        }

        return count;
    }

}
