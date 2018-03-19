package algorithms.BinaryTree;

public class Postorder {
    private BinaryTreeNode root;
    private StringBuilder builder;
    private String result;

    public Postorder(BinaryTreeNode root) {
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

        traverse(node.getLeftChild());

        traverse(node.getRightChild());

        builder.append(node.getValue() + " ");
    }
}
