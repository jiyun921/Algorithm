package bfs;

import java.io.*;
import java.util.*;

public class BOJ5014 {
    static int F;
    static int U;
    static int D;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        F = Integer.parseInt(st.nextToken());
        int S = Integer.parseInt(st.nextToken());
        int G = Integer.parseInt(st.nextToken());
        U = Integer.parseInt(st.nextToken());
        D = Integer.parseInt(st.nextToken());

        visited = new boolean[F+1];

        int result = bfs(S,G);
        System.out.println(result==-1 ? "use the stairs" : result);
    }

    static int bfs(int start, int goal) {
        int count = 0;
        Queue<Integer> queue = new ArrayDeque<>();
        queue.offer(start);
        visited[start]=true;

        while (!queue.isEmpty()) {
            int queueSize = queue.size();
            for (int i=0; i<queueSize; i++) {
                int current = queue.poll();

                if (current == goal) {
                    return count;
                }

                int next1 = current+U;
                int next2 = current-D;

                if (1<=next1 && next1<=F && !visited[next1]) {
                    queue.offer(next1);
                    visited[next1] = true;
                }
                if (1<=next2 && next2<=F && !visited[next2]) {
                    queue.offer(next2);
                    visited[next2] = true;
                }

            }
            count++;
        }

        return -1;

    }
}
