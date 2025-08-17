package bfs;

import java.io.*;
import java.util.*;

public class BOJ5014 {
    static int F;
    static int U;
    static int D;
    static List<Integer> visited = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        F = Integer.parseInt(st.nextToken());
        int S = Integer.parseInt(st.nextToken());
        int G = Integer.parseInt(st.nextToken());
        U = Integer.parseInt(st.nextToken());
        D = Integer.parseInt(st.nextToken());

        int result = bfs(S,G);
        System.out.println(result==-1 ? "use the stairs" : result);
    }

    static int bfs(int start, int goal) {
        int count = 0;
        Queue<Integer> queue = new ArrayDeque<>();
        queue.offer(start);
        visited.add(start);

        while (!queue.isEmpty()) {
            int queueSize = queue.size();
            for (int i=0; i<queueSize; i++) {
                int current = queue.poll();

                if (current == goal) {
                    return count;
                }

                int next1 = current+U;
                int next2 = current-D;

                if (1<=next1 && next1<=F && !visited.contains(next1)) {
                    queue.offer(next1);
                    visited.add(next1);
                }
                if (1<=next2 && next2<=F && !visited.contains(next2)) {
                    queue.offer(next2);
                    visited.add(next2);
                }

            }
            count++;
        }

        return -1;

    }
}
