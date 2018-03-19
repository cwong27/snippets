package algorithms.graph;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

public class NodeTranslatorTest {
    Node root;
    NodeTranslators.NodeTranslator translator = new NodeTranslators.NodeTranslator();

    @Before
    public void setUp() {
        root = translator.from("1,2,1,3,1,4,2,5,2,6,5,9,5,10,4,7,4,8,7,11,7,12");
    }

    @Test
    public void testNodeTranslator() {
        BreadthFirstSearch bfs = new BreadthFirstSearch(root);
        Assert.assertEquals("1 2 3 4 5 6 7 8 9 10 11 12 ", bfs.getResult());
    }
}
