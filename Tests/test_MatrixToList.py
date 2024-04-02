import unittest
import sys
sys.path.append("..")
from Tasks.MatrixToList import mat_to_list

class TestMatToList(unittest.TestCase):
    def test_empty_matrix(self):
        """Test conversion of an empty matrix"""
        adj_mat = []
        result = mat_to_list(adj_mat)
        expected = []
        self.assertEqual(result, expected)

    def test_single_node(self):
        """Test conversion of a matrix with a single node"""
        adj_mat = [[0]]
        result = mat_to_list(adj_mat)
        expected = [[]]
        self.assertEqual(result, expected)

    def test_two_nodes_no_edges(self):
        """Test conversion of a matrix with two nodes and no edges"""
        adj_mat = [[0, 0],
                   [0, 0]]
        result = mat_to_list(adj_mat)
        expected = [[], []]
        self.assertEqual(result, expected)

    def test_two_nodes_one_edge(self):
        """Test conversion of a matrix with two nodes and one edge"""
        adj_mat = [[0, 1],
                   [0, 0]]
        result = mat_to_list(adj_mat)
        expected = [[1], []]
        self.assertEqual(result, expected)

    def test_three_nodes_no_edges(self):
        """Test conversion of a matrix with three nodes and no edges"""
        adj_mat = [[0, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0]]
        result = mat_to_list(adj_mat)
        expected = [[], [], []]
        self.assertEqual(result, expected)

    def test_three_nodes_three_edges(self):
        """Test conversion of a matrix with three nodes and three edges"""
        adj_mat = [[0, 1, 1],
                   [1, 0, 1],
                   [1, 1, 0]]
        result = mat_to_list(adj_mat)
        expected = [[1, 2], [0, 2], [0, 1]]
        self.assertEqual(result, expected)

    def test_four_nodes_four_edges(self):
        """Test conversion of a matrix with four nodes and four edges"""
        adj_mat = [[0, 1, 0, 1],
                   [1, 0, 1, 0],
                   [0, 1, 0, 1],
                   [1, 0, 1, 0]]
        result = mat_to_list(adj_mat)
        expected = [[1, 3], [0, 2], [1, 3], [0, 2]]
        self.assertEqual(result, expected)

    def test_five_nodes_five_edges(self):
        """Test conversion of a matrix with five nodes and five edges"""
        adj_mat = [[0, 1, 0, 0, 1],
                   [1, 0, 1, 0, 0],
                   [0, 1, 0, 1, 0],
                   [0, 0, 1, 0, 1],
                   [1, 0, 0, 1, 0]]
        result = mat_to_list(adj_mat)
        expected = [[1, 4], [0, 2], [1, 3], [2, 4], [0, 3]]
        self.assertEqual(result, expected)

    def test_six_nodes(self):
        """Testing for the given matrix example"""
        adj_mat = [[0, 1, 0, 1, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0],
                [0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0]]
        result = mat_to_list(adj_mat)
        expected = [[1, 3], [2], [0], [4], [3], []]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
