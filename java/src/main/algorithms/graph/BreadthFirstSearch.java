package algorithms.graph;

import java.util.Collection;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.Queue;

public class BreadthFirstSearch {
    private Node root;
    private StringBuilder builder;
    private String result;

    public BreadthFirstSearch(Node root) {
        this.root = root;
        builder = new StringBuilder();
        bfs(this.root);
        result = builder.toString();
    }

    public String getResult() {
        return result;
    }

    private void bfs(Node root) {
        Queue<Node> queue = new LinkedList<>();
        queue.add(root);

        while (!queue.isEmpty()) {
            Node current = queue.poll();
            builder.append(current.getValue() + " ");

            for(Node next : current.getEdges()) {
                queue.add(next);
            }
        }
    }
}
