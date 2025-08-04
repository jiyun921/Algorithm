package dfs;

import java.io.*;
import java.util.*;

public class BOJ1707 {
    static List<Integer>[] graph;
    static boolean[] visited;
    static boolean[] group;
    static StringBuilder sb;
    static boolean isSuccess;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        sb = new StringBuilder();

        int k = Integer.parseInt(br.readLine());
        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine());
            int V = Integer.parseInt(st.nextToken());
            int E = Integer.parseInt(st.nextToken());

            graph = new ArrayList[V + 1];
            for (int j = 1; j <= V; j++) {
                graph[j] = new ArrayList<>();
            }
            visited = new boolean[V + 1];
            group = new boolean[V+1];

            for (int j = 0; j < E; j++) {
                st = new StringTokenizer(br.readLine());
                int u = Integer.parseInt(st.nextToken());
                int v = Integer.parseInt(st.nextToken());
                graph[u].add(v);
                graph[v].add(u);
            }

            isSuccess= true;

            for (int x = 1; x <= V; x++) {
                if (!visited[x]) {
                    dfs(x, true);
                }
            }

            sb.append(isSuccess ? "YES\n" : "NO\n");
        }
        System.out.print(sb);


    }

    static void dfs(int node, boolean div1) {
        if (!isSuccess) return;

        visited[node] = true;
        group[node] = div1;

        for (int next : graph[node]) {
            if (!visited[next]) {
                dfs(next, !div1);
            } else if (group[next]==div1) {
                isSuccess = false;
                return;
            }
        }
    }

}
