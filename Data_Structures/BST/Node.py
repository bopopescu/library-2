

class Node:
    def __init__(self, value):
        print("Node created")
        self.root = value
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        if self.root == data:
            return False

        elif self.root > data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True
        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True

    def find(self, data):
        if self.root == data:
            return True
        elif self.root > data:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False

class Tree:
    def __init__(self):
        print("Tree Initialized")
        self.root = None

    def insert(self, data):
        # if root is not null, insert into tree
        if self.root:
            self.root.insert(data)
            #if root is null, insert root
        else:
            self.root = Node(data)
            return True

    def find(self, value):
        if self.root:
            return self.root.find(value)
        else:
            return False


if __name__ == "__main__":
    numbers = [5,3,2,6,7,9,4,1,8]
    tree = Tree()
    for num in numbers:
        tree.insert(num)

    f = tree.find(10)
    print(f)
    tree.insert(10)
    r = tree.find(10)
    print(r)