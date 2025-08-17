package bfs;

import java.io.*;
import java.util.*;

public class BOJ16953 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());

        System.out.println(bfs(A, B));
    }

    static int bfs(int start, int goal) {
        int count = 1;
        Queue<Integer> queue = new ArrayDeque<>();
        queue.offer(start);

        while (!queue.isEmpty()) {
            int queueSize = queue.size();
            for (int i=0; i<queueSize; i++) {
                int current = queue.poll();

                if (current == goal) {
                    return count;
                }

                int next1 = current*2;
                int next2 = Integer.parseInt(String.valueOf(current) +"1");

                if (next1 <= goal) {
                    queue.offer(next1);
                }
                if (next2 <= goal) {
                    queue.offer(next2);
                }
            }
            count++;
        }

        return -1;
    }

}
