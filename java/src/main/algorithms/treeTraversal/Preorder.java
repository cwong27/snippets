package algorithms.treeTraversal;

public class Preorder {
    private TreeNode root;
    private StringBuilder builder;
    private String result;

    public Preorder(TreeNode root) {
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

        builder.append(node.getValue() + " ");

        traverse(node.getLeftChild());

        traverse(node.getRightChild());
    }
}
