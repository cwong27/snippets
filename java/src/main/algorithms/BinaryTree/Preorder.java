package algorithms.BinaryTree;

public class Preorder {
    private BinaryTreeNode root;
    private StringBuilder builder;
    private String result;

    public Preorder(BinaryTreeNode root) {
        this.root = root;
        builder = new StringBuilder();
        traverse(this.root);
        result = builder.toString();
    }

    public String getResult() {
        return result;
    }

    private void traverse(BinaryTreeNode node) {
        if(node == null) {
            return;
        }

        builder.append(node.getValue() + " ");

        traverse(node.getLeftChild());

        traverse(node.getRightChild());
    }
}
