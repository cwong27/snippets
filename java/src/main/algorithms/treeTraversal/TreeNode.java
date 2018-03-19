package algorithms.treeTraversal;

public class TreeNode {
    public TreeNode(String value) {
        this.value = value;
        this.leftChild = null;
        this.rightChild = null;
    }

    public TreeNode(String value, TreeNode leftChild, TreeNode rightChild) {
        this.value = value;
        this.leftChild = leftChild;
        this.rightChild = rightChild;
    }

    public String getValue() {
        return value;
    }

    public TreeNode getLeftChild() {
        return leftChild;
    }

    public TreeNode getRightChild() {
        return rightChild;
    }

    private String value;
    private TreeNode leftChild;
    private TreeNode rightChild;

}
