from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_from_list(node_values: List[int], current_index: int, total_nodes: int) -> Optional[TreeNode]:
    if current_index < total_nodes:
        node = TreeNode(node_values[current_index])
        node.left = build_tree_from_list(node_values, 2 * current_index + 1, total_nodes)
        node.right = build_tree_from_list(node_values, 2 * current_index + 2, total_nodes)

        return node

    return None
