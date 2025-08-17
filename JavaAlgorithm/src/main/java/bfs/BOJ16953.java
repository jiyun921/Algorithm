package bfs;

import java.io.*;
import java.util.*;

public class BOJ16953 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        long A = Integer.parseInt(st.nextToken());
        long B = Integer.parseInt(st.nextToken());

        System.out.println(bfs(A, B));
    }

    static int bfs(long start, long goal) {
        int count = 1;
        Queue<Long> queue = new ArrayDeque<>();
        queue.offer(start);

        while (!queue.isEmpty()) {
            int queueSize = queue.size();
            for (int i=0; i<queueSize; i++) {
                long current = queue.poll();

                if (current == goal) {
                    return count;
                }

                long next1 = current*2;
                long next2 = Long.parseLong(String.valueOf(current) +"1");

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