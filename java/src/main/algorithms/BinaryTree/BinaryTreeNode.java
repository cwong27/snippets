package algorithms.BinaryTree;

import algorithms.graph.Node;

import java.util.HashMap;

public class BinaryTreeNode {

    public static class Translator {
        public BinaryTreeNode from(String input) {
            return from(input.split(","));
        }

        public BinaryTreeNode from(String[] inputs) {
            if(inputs.length < 3) {
                return null;
            }

            BinaryTreeNode root = new BinaryTreeNode(inputs[0]);
            BinaryTreeNode child = new BinaryTreeNode(inputs[1]);
            if(inputs[2].equalsIgnoreCase("L")) {
                root.leftChild = child;
            } else {
                root.rightChild = null;
            }
            child.leftChild = null;
            child.rightChild = null;

            HashMap<String, BinaryTreeNode> nodes = new HashMap<>();
            nodes.put(inputs[0], root);
            nodes.put(inputs[1], child);

            for(int i = 3; i < inputs.length; i+=3) {
                BinaryTreeNode node1;
                BinaryTreeNode node2;

                if(!nodes.containsKey(inputs[i])) {
                    node1 = new BinaryTreeNode(inputs[i]);
                    node1.leftChild = null;
                    node1.rightChild = null;
                    nodes.put(inputs[i], node1);
                } else {
                    node1 = nodes.get(inputs[i]);
                }

                if(!nodes.containsKey(inputs[i+1])) {
                    node2 = new BinaryTreeNode(inputs[i+1]);
                    node2.leftChild = null;
                    node2.rightChild = null;
                    nodes.put(inputs[i+1], node2);
                } else {
                    node2 = nodes.get(inputs[i+1]);
                }

                if(inputs[i+2].equalsIgnoreCase("L")) {
                    node1.leftChild = node2;
                } else {
                    node1.rightChild = node2;
                }
            }

            return root;
        }
    }

    public BinaryTreeNode(String value) {
        this.value = value;
        this.leftChild = null;
        this.rightChild = null;
    }

    public BinaryTreeNode(String value, BinaryTreeNode leftChild, BinaryTreeNode rightChild) {
        this.value = value;
        this.leftChild = leftChild;
        this.rightChild = rightChild;
    }

    public String getValue() {
        return value;
    }

    public BinaryTreeNode getLeftChild() {
        return leftChild;
    }

    public BinaryTreeNode getRightChild() {
        return rightChild;
    }

    private String value;
    private BinaryTreeNode leftChild;
    private BinaryTreeNode rightChild;

}
