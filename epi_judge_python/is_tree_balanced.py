from test_framework import generic_test


def is_balanced_binary_tree(tree):
    def is_balanced_binary_helper(node):
        if not node:
            return 0
        left, right =  is_balanced_binary_helper(node.left) , is_balanced_binary_helper(node.right)
        if left == -1 or right == -1 or abs(left-right) > 1:
            return -1
        else:
            return max(left, right) + 1

    return is_balanced_binary_helper(tree) != -1




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
