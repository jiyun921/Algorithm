package dfs;

import java.io.*;
import java.util.*;

public class BOJ2644 {

    static List<Integer>[] graph;
    static boolean[] visited;
    static int goalB;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int goalA = Integer.parseInt(st.nextToken());
        goalB = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int m = Integer.parseInt(st.nextToken());

        graph = new ArrayList[n+1];
        for (int i=0; i<n+1; i++) {
            graph[i] = new ArrayList<>();
        }
        visited = new boolean[n+1];

        for (int i=0; i<m; i++) {
            st = new StringTokenizer(br.readLine());
            int parent = Integer.parseInt(st.nextToken());
            int child = Integer.parseInt(st.nextToken());
            graph[parent].add(child);
            graph[child].add(parent);
        }

        System.out.println(dfs(goalA,0));

    }

    static int dfs(int node, int depth) {
        if (node==goalB) return depth;

        visited[node] = true;

        for (int next : graph[node]) {
            if (!visited[next]) {
                int result = dfs(next, depth+1);
                if (result!=-1) return result;
            }
        }

        return -1;
    }
}
