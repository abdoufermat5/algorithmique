import math


class Node(object):
    def __init__(self, order):
        self.order = order
        self.values = []
        self.keys = []
        self.nextKey = None
        self.parent = None
        self.check_leaf = False

    def insert_at_leaf(self, leaf, value, key):
        if self.values:
            temp1 = self.values
            for i in range(len(temp1)):
                if temp1[i] == value:
                    self.keys[i].append(key)
                    break
                elif temp1[i] > value:
                    self.values.insert(i, value)
                    self.keys.insert(i, [key])
                    break
                elif i == len(temp1) - 1:
                    self.values.append(value)
                    self.keys.append([key])
                    break
        else:
            self.values.append(value)
            self.keys.append([key])


class BPlusTree:
    def __init__(self, order):
        self.root = Node(order)
        self.root.check_leaf = True

    def insert(self, value, key):
        value = str(value)
        old_node = self.search(value)
        old_node.insert_at_leaf(old_node, value, key)

        if len(old_node.values) == old_node.order:
            new_node = Node(old_node.order)
            new_node.check_leaf = True
            new_node.parent = old_node.parent
            mid = math.ceil(old_node.order / 2)
            new_node.values = old_node.values[mid:]
            new_node.keys = old_node.keys[mid:]
            old_node.values = old_node.values[:mid]
            old_node.keys = old_node.keys[:mid]
            if old_node.nextKey:
                new_node.nextKey = old_node.nextKey
            old_node.nextKey = new_node
            if old_node.parent:
                self.insert_in_parent(old_node, new_node.values[0], new_node)
            else:
                self.create_new_root(old_node, new_node.values[0], new_node)

    def search(self, value):
        current_node = self.root
        while not current_node.check_leaf:
            temp2 = current_node.values
            for i in range(len(temp2)):
                if temp2[i] == value:
                    current_node = current_node.keys[i + 1]
                    break
                elif temp2[i] > value:
                    current_node = current_node.keys[i]
                    break
                elif i == len(temp2) - 1:
                    current_node = current_node.keys[i + 1]
                    break
        return current_node

    def insert_in_parent(self, n, value, ndash):
        if self.root == n:
            rootNode = Node(n.order)
            rootNode.values.append(value)
            rootNode.keys.append(n)
            rootNode.keys.append(ndash)
            self.root = rootNode
            n.parent = rootNode
            ndash.parent = rootNode
            return

        parentNode = n.parent
        temp3 = parentNode.keys

        for i in range(len(temp3)):
            if temp3[i] == n:
                parentNode.values.insert(i, value)
                parentNode.keys.insert(i + 1, ndash)

                if len(parentNode.keys) > parentNode.order:
                    parentDash = Node(parentNode.order)
                    parentDash.parent = parentNode.parent
                    mid = math.ceil(parentNode.order / 2)
                    parentDash.values = parentNode.values[mid:]
                    parentDash.keys = parentNode.keys[mid:]
                    value_ = parentNode.values[mid + 1]

                    if mid == 0:
                        parentNode.values = parentNode.values[:mid]
                    else:
                        parentNode.values = parentNode.values[:mid - 1]
                    parentNode.keys = parentNode.keys[:mid]
                    for j in parentNode.keys:
                        j.parent = parentNode
                    for j in parentDash.keys:
                        j.parent = parentDash
                    self.insert_in_parent(parentNode, value_, parentDash)

    def create_new_root(self, old_node, param, new_node):
        rootNode = Node(old_node.order)
        rootNode.values.append(param)
        rootNode.keys.append(old_node)
        rootNode.keys.append(new_node)
        old_node.parent = rootNode
        new_node.parent = rootNode
        self.root = rootNode

    def find(self, value, key):
        node = self.search(value)
        if value in node.values:
            index = node.values.index(value)
            if key in node.keys[index]:
                return True
        return False


def printTree(tree):
    lst = [tree.root]
    level = [0]
    leaf = None
    flag = 0
    lev_leaf = 0

    node1 = Node(str(level[0]) + str(tree.root.values))

    while len(lst) != 0:
        x = lst.pop(0)
        lev = level.pop(0)
        if not x.check_leaf:
            for i, item in enumerate(x.keys):
                print(item.values)
        else:
            for i, item in enumerate(x.keys):
                print(item.values)
            if flag == 0:
                leaf = x
                lev_leaf = lev
                flag = 1


if __name__ == '__main__':
    record_len = 3
    bplustree = BPlusTree(record_len)
    bplustree.insert('5', '33')
    bplustree.insert('15', '21')
    bplustree.insert('25', '31')
    bplustree.insert('35', '41')
    bplustree.insert('45', '10')
    printTree(bplustree)

    if bplustree.find('45', '11'):
        print("Found")
    else:
        print("Not found")
