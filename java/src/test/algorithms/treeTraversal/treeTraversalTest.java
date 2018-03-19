package algorithms.treeTraversal;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

public class treeTraversalTest {
    private static treeNode testRoot;

    @Before
    public void setUp() {
        treeNode nodeC = new treeNode("C");
        treeNode nodeE = new treeNode("E");
        treeNode nodeH = new treeNode("H");

        treeNode nodeD = new treeNode("D", nodeC, nodeE);
        treeNode nodeA = new treeNode("A");
        treeNode nodeB = new treeNode("B", nodeA, nodeD);

        treeNode nodeI = new treeNode("I", nodeH, null);
        treeNode nodeG = new treeNode("G", null, nodeI);

        testRoot = new treeNode("F", nodeB, nodeG);
    }

    @Test
    public void testInOrder() {
        inorder test = new inorder(testRoot);
        Assert.assertEquals("A B C D E F G H I ", test.getResult());
    }

    @Test
    public void testPreOrder() {
        preorder test = new preorder(testRoot);
        Assert.assertEquals("F B A D C E G I H ", test.getResult());
    }

    @Test
    public void testPostOrder() {
        postorder test = new postorder(testRoot);
        Assert.assertEquals("A C E D B H I G F ", test.getResult());
    }
}
