package algorithms.graph;

import java.util.ArrayList;
import java.util.List;

public class Node {
    private List<Node> edges;
    private String value;

    public Node(String value) {
        this.value = value;
        edges = new ArrayList<>();
    }

    public String getValue() {
        return value;
    }

    public List<Node> getEdges() {
        return edges;
    }

    public void addEdge(Node node) {
        edges.add(node);
    }
}
