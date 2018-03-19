package algorithms.treeTraversal;

public class treeNode {
    public treeNode(String value) {
        this.value = value;
        this.leftChild = null;
        this.rightChild = null;
    }

    public treeNode(String value, treeNode leftChild, treeNode rightChild) {
        this.value = value;
        this.leftChild = leftChild;
        this.rightChild = rightChild;
    }

    public String getValue() {
        return value;
    }

    public treeNode getLeftChild() {
        return leftChild;
    }

    public treeNode getRightChild() {
        return rightChild;
    }

    private String value;
    private treeNode leftChild;
    private treeNode rightChild;

}
