import pytest
from common.tree_node import build_tree_from_list
from solutions.problem_0129 import Solution


@pytest.fixture
def solution():
    return Solution()


def test_sumNumbers_testcase1(solution):
    tree_values = [1, 2, 3]
    root = build_tree_from_list(tree_values, 0, len(tree_values))

    assert solution.sumNumbers(root) == 25


def test_sumNumbers_testcase2(solution):
    tree_values = [4, 9, 0, 5, 1]
    root = build_tree_from_list(tree_values, 0, len(tree_values))

    assert solution.sumNumbers(root) == 1026
