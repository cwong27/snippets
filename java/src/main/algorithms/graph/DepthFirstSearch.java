package algorithms.graph;

import java.util.Stack;

public class DepthFirstSearch {
    private Node root;
    private StringBuilder builder;
    private String result;

    public DepthFirstSearch(Node root) {
        this.root = root;
        builder = new StringBuilder();
        dfs(this.root);
        result = builder.toString();
    }

    public String getResult() {
        return result;
    }

    private void dfs(Node root) {
        Stack<Node> stack = new Stack<>();
        stack.push(root);

        while(!stack.isEmpty()) {
            Node current = stack.pop();

            builder.append(current.getValue() + " ");

            for(Node next : current.getEdges()) {
                stack.push(next);
            }
        }
    }
}
