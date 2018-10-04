class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.data = val

def binary_insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.l_child is None:
                root.l_child = node
            else:
                binary_insert(root.l_child, node)
        else:
            if root.r_child is None:
                root.r_child = node
            else:
                binary_insert(root.r_child, node)

def in_order_print(root):
    if not root:
        return
    in_order_print(root.l_child)
    print (root.data)
    in_order_print(root.r_child)

def pre_order_print(root):
    if not root:
        return
    print (root.data)
    pre_order_print(root.l_child)
    pre_order_print(root.r_child)


num_list = (4, 8, 2, 6, 9, 7, 1, 3)

root = Node(5)


for i in num_list:
    node = Node(i)
    binary_insert(root, node)

pre_order_print(root)
