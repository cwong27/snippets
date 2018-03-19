package algorithms.BinaryTree;

public class Inorder {
    private BinaryTreeNode root;
    private StringBuilder builder;
    private String result;

    public Inorder(BinaryTreeNode root) {
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

        builder.append(node.getValue() + " ");

        traverse(node.getRightChild());
    }
}
