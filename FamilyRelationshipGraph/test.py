import unittest
from Colormap import Colormap
from Edge_Length import Edge_Length

class TestColorMap(unittest.TestCase):

    def test_NotEmptyNodes(self):
        color = Colormap()
        color.create_nodes('test_nodes.txt')
        self.assertTrue(color.get_nodes())

    def test_NotEmptyFeatures(self):
        color = Colormap()
        color.create_nodes('test_nodes.txt')
        self.assertTrue(color.get_features())

    def test_correctnodes(self):
        nodes = [0,1,2,3,4]
        color = Colormap()
        color.create_nodes('test_nodes.txt')
        self.assertCountEqual(nodes, color.get_nodes())

    def test_correctfeatures(self):
        features = [0,1,2,3,4]
        color = Colormap()
        color.create_nodes('test_nodes.txt')
        self.assertCountEqual(features,color.get_features())

if __name__ == '__main__':
    unittest.main()