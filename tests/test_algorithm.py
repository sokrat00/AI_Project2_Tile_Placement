import unittest
from backtracking import solve
from landscape import Landscape
from input import Tile_input


class TestAlgo(unittest.TestCase):
    """Tests whether the result found by algorithm is correct"""
    def test_solver(self):
        tile_input = Tile_input('../inputs/tilesproblem_1327003802793100.txt')
        landscape = Landscape(tile_input)
        targets = landscape.targets
        print(landscape)
        print(targets)
        solve(landscape, 0, 0)
        result = landscape.current
        print(landscape)
        print(result)
        self.assertEqual(targets, result)


if __name__ == '__main__':
    unittest.main()