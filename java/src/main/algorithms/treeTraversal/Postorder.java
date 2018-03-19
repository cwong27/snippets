package algorithms.treeTraversal;

public class Postorder {
    private TreeNode root;
    private StringBuilder builder;
    private String result;

    public Postorder(TreeNode root) {
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

        traverse(node.getRightChild());

        builder.append(node.getValue() + " ");
    }
}
