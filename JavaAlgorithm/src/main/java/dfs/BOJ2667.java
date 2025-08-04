package dfs;
import java.io.*;
import java.util.*;

public class BOJ2667 {
    static int[][] graph;
    static boolean[][] visited;
    static int n;
    static int AptNum;
    static int AptCnt;
    static final int[] dx = {-1,1,0,0};
    static final int[] dy = {0,0,-1,1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        graph = new int[n][n];
        visited = new boolean[n][n];

        for (int i=0; i<n; i++) {
            String line = br.readLine();
            for (int j=0; j<n; j++) {
                graph[i][j] = line.charAt(j) - '0';
            }
        }


        AptNum=0;
        List<Integer> AptCntList = new ArrayList();

        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                if (!visited[i][j] && graph[i][j]==1) {
                    AptNum++;
                    AptCnt=1;
                    dfs(i,j);
                    AptCntList.add(AptCnt);
                }
            }
        }

        Collections.sort(AptCntList);
        StringBuilder sb = new StringBuilder();
        sb.append(AptNum).append('\n');
        for (int aptcnt : AptCntList) {
            sb.append(aptcnt).append('\n');
        }
        System.out.print(sb);

    }

    static void dfs(int x, int y) {
        visited[x][y] = true;
        graph[x][y] = AptNum;

        for (int i=0; i<4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (0<=nx && nx<n && 0<=ny && ny<n) {
                if (!visited[nx][ny] && graph[nx][ny]==1) {
                    AptCnt++;
                    dfs(nx,ny);
                }
            }
        }
    }
}
