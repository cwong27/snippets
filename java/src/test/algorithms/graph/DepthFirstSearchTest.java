package algorithms.graph;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

public class DepthFirstSearchTest {
    Node root;

    @Before
    public void setUp() {
        root = new Node("1");
        Node node2 = new Node("2");
        Node node3 = new Node("3");
        Node node4 = new Node("4");
        Node node5 = new Node("5");
        Node node6 = new Node("6");
        Node node7 = new Node("7");
        Node node8 = new Node("8");
        Node node9 = new Node("9");
        Node node10 = new Node("10");
        Node node11 = new Node("11");
        Node node12 = new Node("12");

        root.addEdge(node8);
        root.addEdge(node7);
        root.addEdge(node2);

        node2.addEdge(node6);
        node2.addEdge(node3);

        node3.addEdge(node5);
        node3.addEdge(node4);

        node8.addEdge(node12);
        node8.addEdge(node9);

        node9.addEdge(node11);
        node9.addEdge(node10);
    }

    @Test
    public void testBreadthFirstSearch() {
        DepthFirstSearch dfs = new DepthFirstSearch(root);
        Assert.assertEquals("1 2 3 4 5 6 7 8 9 10 11 12 ", dfs.getResult());
    }
}
