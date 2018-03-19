package algorithms.BinaryTree;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

public class BinaryTreeTest {
    private static BinaryTreeNode testRoot;
    private static BinaryTreeNode.Translator translator = new BinaryTreeNode.Translator();

    @Before
    public void setUp() {
//        BinaryTreeNode nodeC = new BinaryTreeNode("C");
//        BinaryTreeNode nodeE = new BinaryTreeNode("E");
//        BinaryTreeNode nodeH = new BinaryTreeNode("H");
//
//        BinaryTreeNode nodeD = new BinaryTreeNode("D", nodeC, nodeE);
//        BinaryTreeNode nodeA = new BinaryTreeNode("A");
//        BinaryTreeNode nodeB = new BinaryTreeNode("B", nodeA, nodeD);
//
//        BinaryTreeNode nodeI = new BinaryTreeNode("I", nodeH, null);
//        BinaryTreeNode nodeG = new BinaryTreeNode("G", null, nodeI);
//
//        testRoot = new BinaryTreeNode("F", nodeB, nodeG);

        testRoot = translator.from(
                "F,B,L," +
                        "F,G,R," +
                        "B,A,L," +
                        "B,D,R," +
                        "D,C,L," +
                        "D,E,R," +
                        "G,I,R," +
                        "I,H,L");
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
