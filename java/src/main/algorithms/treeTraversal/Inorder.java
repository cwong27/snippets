package algorithms.treeTraversal;

public class Inorder {
    private TreeNode root;
    private StringBuilder builder;
    private String result;

    public Inorder(TreeNode root) {
        this.root = root;
        builder = new StringBuilder();
        traverse(this.root);
        result = builder.toString();
    }

    public String getResult() {
        return result;
    }

    private void traverse(TreeNode node) {
        if(node == null) {
            return;
        }

        traverse(node.getLeftChild());

        builder.append(node.getValue() + " ");

        traverse(node.getRightChild());
    }
}
