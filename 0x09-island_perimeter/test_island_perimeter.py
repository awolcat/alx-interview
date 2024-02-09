import unittest
island_perimeter = __import__('0-island_perimeter').island_perimeter

class TestIslandPerimeter(unittest.TestCase):
    """Tester
    """
    def test_perfect_island(self):

        grid = [
                [0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0],
                [0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0]
            ]
        self.assertEqual(island_perimeter(grid), 12)

        grid = [[0, 0, 0, 0, 0, 0],[0, 1, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0]]
        self.assertEqual(island_perimeter(grid), 4)

    def test_no_island(self):
        grid = [[0, 0, 0, 1],
                [0, 0, 0, 0,]]
        self.assertEqual(island_perimeter(grid), 0)

    def test_all_water(self):
        grid = [[0],[0],[0]]
        self.assertEqual(island_perimeter(grid), 0)

    def test_all_land(self):
        grid = [[1, 1, 1, 1, 1],[1, 1, 1, 1, 1],[1, 1, 1, 1, 1]]
        self.assertEqual(island_perimeter(grid), 0)

    def test_not_an_island(self):
        grid = [[0, 0, 0, 0, 0, 0],
                [0, 1, 1, 0, 0, 0],
                [1, 1, 1, 0, 0, 0],
                [0, 1, 1, 1, 0, 0],
                [0, 0, 0, 1, 1, 1]]
        self.assertEqual(island_perimeter(grid), 20)

    def test_my_island(self):
        grid = [[0, 1, 0, 0, 0, 1],
                [1, 1, 0, 0, 0, 1],
                [1, 1, 0, 1, 1, 1],
                [0, 1, 1, 1, 0, 0],
                [0, 0, 1, 1, 0, 0]]
        self.assertEqual(island_perimeter(grid), 28)
