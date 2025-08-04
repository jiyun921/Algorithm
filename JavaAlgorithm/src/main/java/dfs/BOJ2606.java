package dfs;

import java.io.*;
import java.util.*;

public class BOJ2606 {
    static List<Integer>[] graph;
    static boolean[] visited;
    static int count;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int PcCount = Integer.parseInt(br.readLine());
        int PcPairCount = Integer.parseInt(br.readLine());

        graph = new ArrayList[PcCount+1];
        visited = new boolean[PcCount+1];

        for (int i = 1; i <= PcCount; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i=0; i<PcPairCount; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[a].add(b);
            graph[b].add(a);
        }

        count = 0;

        dfs(1);

        System.out.println(count);

    }

    static void dfs(int node) {
        visited[node] = true;
        for (int next : graph[node]) {
            if (!visited[next]) {
                dfs(next);
                count++;
            }
        }
    }
}
