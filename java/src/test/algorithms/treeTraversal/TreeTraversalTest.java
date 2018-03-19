package algorithms.treeTraversal;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

public class TreeTraversalTest {
    private static TreeNode testRoot;

    @Before
    public void setUp() {
        TreeNode nodeC = new TreeNode("C");
        TreeNode nodeE = new TreeNode("E");
        TreeNode nodeH = new TreeNode("H");

        TreeNode nodeD = new TreeNode("D", nodeC, nodeE);
        TreeNode nodeA = new TreeNode("A");
        TreeNode nodeB = new TreeNode("B", nodeA, nodeD);

        TreeNode nodeI = new TreeNode("I", nodeH, null);
        TreeNode nodeG = new TreeNode("G", null, nodeI);

        testRoot = new TreeNode("F", nodeB, nodeG);
    }

    @Test
    public void testInOrder() {
        Inorder test = new Inorder(testRoot);
        Assert.assertEquals("A B C D E F G H I ", test.getResult());
    }

    @Test
    public void testPreOrder() {
        Preorder test = new Preorder(testRoot);
        Assert.assertEquals("F B A D C E G I H ", test.getResult());
    }

    @Test
    public void testPostOrder() {
        Postorder test = new Postorder(testRoot);
        Assert.assertEquals("A C E D B H I G F ", test.getResult());
    }
}
