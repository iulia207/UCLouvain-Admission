import unittest
import sys
sys.path.append("..")
from Tasks.ReachableNodes import reachable

class TestReachable(unittest.TestCase):
    def test_single_node(self):
        """Test reachable with a single node"""
        adj_list = {0: []}
        start_node = 0
        expected = {0}
        result = reachable(adj_list, start_node)
        self.assertEqual(result, expected)

    def test_simple_graph(self):
        """Test reachable with a simple graph"""
        adj_list = {
            0: [1, 2],
            1: [2],
            2: [3],
            3: []
        }
        start_node = 0
        expected = {0, 1, 2, 3}
        result = reachable(adj_list, start_node)
        self.assertEqual(result, expected)

    def test_disconnected_graph(self):
        """Test reachable with a disconnected graph"""
        adj_list = {
            0: [1, 2],
            1: [],
            2: [],
            3: []
        }
        start_node = 0
        expected = {0, 1, 2}
        result = reachable(adj_list, start_node)
        self.assertEqual(result, expected)

    def test_cyclic_graph(self):
        """Test reachable with a cyclic graph"""
        adj_list = {
            0: [1],
            1: [2],
            2: [3],
            3: [0]
        }
        start_node = 0
        expected = {0, 1, 2, 3}
        result = reachable(adj_list, start_node)
        self.assertEqual(result, expected)

    def test_given_example_graph_0(self):
        """Test reachable on the given graph starting from 0"""
        adj_list = {
            0: [1, 3],
            1: [2],
            2: [0],
            3: [4],
            4: [3],
            5: []
        }
        start_node = 0
        expected = {0, 1, 2, 3, 4}
        result = reachable(adj_list, start_node)
        self.assertEqual(result, expected)

    def test_given_example_graph_3(self):
        """Test reachable on the given graph starting from 3"""
        adj_list = {
            0: [1, 3],
            1: [2],
            2: [0],
            3: [4],
            4: [3],
            5: []
        }
        start_node = 3
        expected = {3, 4}
        result = reachable(adj_list, start_node)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
