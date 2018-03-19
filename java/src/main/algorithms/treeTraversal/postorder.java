package algorithms.treeTraversal;

public class postorder {
    private treeNode root;
    private StringBuilder builder;
    private String result;

    public postorder(treeNode root) {
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

        traverse(node.getLeftChild());

        traverse(node.getRightChild());

        builder.append(node.getValue() + " ");
    }
}
