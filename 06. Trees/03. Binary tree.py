class BinarySearchTreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            # add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # add data in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []
        # visit left tree
        if self.left:
            elements += self.left.in_order_traversal()
        # visit base node
        elements.append(self.data)
        # visit right node
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers = []
    size = int(input("Enter number of elements: "))
    print("Enter ",size,"elements: ")
    for i in range(size):
        num = int(input())
        numbers.append(num)
    number_tree = build_tree(numbers)
    print(number_tree.in_order_traversal())