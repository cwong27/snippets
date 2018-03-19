package algorithms.treeTraversal;

public class preorder {
    private treeNode root;
    private StringBuilder builder;
    private String result;

    public preorder(treeNode root) {
        this.root = root;
        builder = new StringBuilder();
        traverse(this.root);
        result = builder.toString();
    }

    public String getResult() {
        return result;
    }

    private void traverse(treeNode node) {
        if(node == null) {
            return;
        }

        builder.append(node.getValue() + " ");

        traverse(node.getLeftChild());

        traverse(node.getRightChild());
    }
}
