#!/usr/bin/python3

"""
https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:

    def __init__(self, vals):
        self.root_node = self.form_binary_tree(vals)

    def form_binary_tree(self, vals):
        """
        vals is assumed to be a sorted (ascending) list
        """

        mid = int(len(vals) / 2)
        node = Node(vals[mid])

        if mid > 0:
            left_list = vals[0:mid]
            node.left = self.form_binary_tree(left_list)

        if mid < len(vals) - 1:
            right_list = vals[mid+1:]
            node.right = self.form_binary_tree(right_list)

        return node

    def in_order_traversal(self):
        return self.get_nodes(self.root_node)

    def get_nodes(self, node):
        """
        In-order Traversal,
        for checking only
        """

        if node is None:
            return []

        left_list = self.get_nodes(node.left)
        right_list = self.get_nodes(node.right)

        return left_list + [node.val] + right_list

class RankedNode(Node):

    def __init__(self, val, rank):
        super(RankedNode, self).__init__(val)
        self.rank = rank

class RankedBinaryTree:

    def __init__(self, vals):

        rank_val_tuples = [(idx, val) for idx, val in enumerate(vals)]
        self.root_node = self.form_binary_tree(rank_val_tuples)

    def form_binary_tree(self, rank_val_tuples):

        mid = int(len(rank_val_tuples) / 2)
        val = rank_val_tuples[mid][1]
        rank = rank_val_tuples[mid][0]

        node = RankedNode(val, rank)

        if mid > 0:
            left_tuples = rank_val_tuples[0:mid]
            node.left = self.form_binary_tree(left_tuples)

        if mid < len(rank_val_tuples) - 1:
            right_tuples = rank_val_tuples[mid+1:]
            node.right = self.form_binary_tree(right_tuples)

        return node

    def get_rank(self, val):
        return self.search_rank(self.root_node, val)

    def search_rank(self, node, val):

        if val == node.val:
            return node.rank

        if val < node.val:
            if node.left is None:
                return (node.rank - 1)
            else:
                return self.search_rank(node.left, val)

        elif val > node.val:
            if node.right is None:
                return node.rank
            else:
                return self.search_rank(node.right, val)

if __name__ == "__main__":

    # testing
    ex = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    tree = BinaryTree(ex)
    print(tree.in_order_traversal())

    ex = [1]
    tree = BinaryTree(ex)
    print(tree.in_order_traversal())

    ex = [1, 3, 5, 7]
    tree = RankedBinaryTree(ex)

    for i in range(9):
        print(len(ex) - tree.get_rank(i))


