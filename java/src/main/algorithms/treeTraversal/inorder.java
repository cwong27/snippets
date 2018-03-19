package algorithms.treeTraversal;

public class inorder {
    private treeNode root;
    private StringBuilder builder;
    private String result;

    public inorder(treeNode root) {
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

        builder.append(node.getValue() + " ");

        traverse(node.getRightChild());
    }
}
