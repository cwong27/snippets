package algorithms.graph;

import java.util.HashMap;

public class NodeTranslators {
    public static class NodeTranslator {
        public Node from(String inputs) {
            return from(inputs.split(","));
        }

        public Node from(String[] inputs) {
            if(inputs.length < 2) {
                return null;
            }

            Node root = new Node(inputs[0]);
            Node child = new Node(inputs[1]);
            root.getEdges().add(child);

            HashMap<String, Node> nodes = new HashMap<>();
            nodes.put(inputs[0], root);
            nodes.put(inputs[1], child);

            for(int i = 2; i < inputs.length; i+=2) {
                Node node1;
                Node node2;

                if(!nodes.containsKey(inputs[i])) {
                    node1 = new Node(inputs[i]);
                    nodes.put(inputs[i], node1);
                } else {
                    node1 = nodes.get(inputs[i]);
                }

                if(!nodes.containsKey(inputs[i+1])) {
                    node2 = new Node(inputs[i+1]);
                    nodes.put(inputs[i+1], node2);
                } else {
                    node2 = nodes.get(inputs[i+1]);
                }

                node1.getEdges().add(node2);
            }

            return root;
        }
    }
}
