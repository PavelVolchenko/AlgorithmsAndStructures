from dataclasses import dataclass

@dataclass
class Node:
    value: object = None
    left: object = None
    right: object = None

    def contains(self, value):
        if Node.value is None:
            return False
        return Node.contains(value)


arr = Node(1)
print(arr.contains(1))


"""
public class Tree<V extends Comparable<V>> {
    private Node root;

    private class Node {
        private V value;
        private Node left;
        private Node right;
    }

//    public boolean contains(V value){
//        Node node = root;
//        while (node != null){
//            if (node.value.equals(value)){
//                return true;
//            }
//            if (node.value.compareTo(value) > 0) {
//                node = node.left;
//            }else {
//                node = node.right;
//            }
//        }
//        return false;
//    }

    //решение рекурсией
    public boolean contains(V value) {
        if (root == null){
            return false;
        }
        return contains(root, value);
    }

    private boolean contains(Node node, V value) {
        if (node.value.equals(value)){
            return true;
        } else {
            if (node.value.compareTo(value) > 0){
                return contains(node.left, value);
            } else {
                return contains(node.right, value);
            }
        }
    }
}
"""