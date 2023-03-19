import unittest
import os
import unittest
from input import Tile_input
from landscape import Landscape


class TestLandscape(unittest.TestCase):
    """Tests whether operations on the landscape are done correctly"""
    def test_count_colors(self):
        """Checks whether counting color function is working properly."""
        correct_colors = [{'1': 83, '2': 80, '3': 74, '4': 75},
                          {'1': 77, '2': 72, '3': 65, '4': 94},
                          {'1': 78, '2': 81, '3': 75, '4': 83},
                          {'1': 84, '2': 82, '3': 76, '4': 76},
                          {'1': 77, '2': 69, '3': 90, '4': 77},
                          {'1': 81, '2': 81, '3': 85, '4': 80},
                          {'1': 78, '2': 83, '3': 83, '4': 77},
                          {'1': 65, '2': 94, '3': 80, '4': 74},
                          {'1': 91, '2': 84, '3': 71, '4': 76},
                          {'1': 72, '2': 77, '3': 88, '4': 78},
                          {'1': 75, '2': 71, '3': 85, '4': 88},
                          {'1': 85, '2': 82, '3': 67, '4': 90},
                          {'1': 83, '2': 73, '3': 81, '4': 70},
                          {'1': 77, '2': 83, '3': 75, '4': 76},
                          {'1': 67, '2': 91, '3': 74, '4': 88},
                          {'1': 74, '2': 76, '3': 96, '4': 85}]


        for i, file in enumerate(sorted(os.listdir('../inputs'))):
            tp_input = Tile_input(os.path.join('../inputs', file))
            landscape = Landscape(tp_input)
            self.assertEqual(landscape.count_colors(), correct_colors[i])

    def test_outer_tile(self):
        """Checks whether putting outer tile have the desired result."""
        tp_input = Tile_input('../inputs/tilesproblem_1326658913086500.txt')
        landscape = Landscape(tp_input)

        outer = next((x for x in landscape.tiles if x.type == 'OUTER_BOUNDARY'), None)
        outer_location = (4, 0)
        correct_outer = [[2, 2, 1, 3, 0, 3, 4, 0, 4, 2, 2, 4, 0, 4, 0, 0, 0, 2, 4, 3],
                         [0, 2, 1, 3, 2, 2, 0, 0, 0, 1, 0, 1, 2, 2, 0, 2, 3, 4, 4, 4],
                         [2, 1, 0, 0, 0, 2, 2, 4, 3, 2, 2, 2, 1, 2, 2, 0, 0, 1, 1, 0],
                         [0, 3, 2, 0, 1, 0, 1, 1, 4, 1, 3, 4, 2, 1, 0, 0, 0, 1, 4, 1],
                         [0, 0, 0, 0, 4, 4, 0, 2, 2, 0, 0, 3, 2, 3, 0, 2, 0, 2, 3, 2],
                         [0, 4, 1, 0, 1, 1, 1, 4, 1, 0, 1, 3, 0, 3, 2, 0, 4, 0, 1, 2],
                         [0, 3, 1, 0, 3, 3, 1, 4, 0, 1, 1, 1, 4, 2, 2, 4, 1, 4, 3, 4],
                         [0, 0, 0, 0, 4, 4, 3, 4, 4, 2, 0, 3, 0, 3, 0, 3, 4, 4, 0, 0],
                         [1, 0, 0, 3, 0, 3, 2, 2, 4, 3, 3, 2, 4, 0, 0, 0, 1, 4, 3, 0],
                         [0, 1, 3, 1, 3, 2, 3, 2, 1, 0, 0, 1, 4, 3, 2, 1, 2, 4, 1, 3],
                         [0, 3, 0, 2, 3, 4, 3, 3, 1, 0, 0, 1, 2, 3, 3, 0, 2, 1, 2, 3],
                         [1, 3, 1, 1, 4, 4, 4, 2, 0, 4, 4, 3, 4, 1, 1, 2, 2, 3, 2, 3],
                         [2, 1, 0, 1, 1, 1, 0, 1, 2, 1, 3, 2, 2, 3, 3, 4, 0, 0, 3, 4],
                         [4, 2, 0, 0, 2, 3, 2, 1, 1, 1, 4, 0, 4, 4, 3, 2, 2, 0, 2, 3],
                         [3, 1, 4, 3, 0, 1, 4, 4, 1, 1, 3, 1, 1, 1, 0, 0, 2, 1, 2, 0],
                         [3, 2, 2, 4, 3, 1, 1, 4, 1, 0, 0, 3, 1, 2, 3, 2, 2, 2, 3, 4],
                         [0, 2, 2, 1, 3, 3, 1, 1, 0, 0, 0, 3, 0, 4, 4, 2, 2, 2, 4, 4],
                         [0, 1, 4, 3, 0, 0, 1, 1, 3, 3, 0, 4, 3, 4, 4, 4, 4, 1, 1, 1],
                         [3, 2, 1, 2, 0, 3, 1, 1, 3, 4, 2, 4, 0, 3, 0, 2, 0, 0, 4, 1],
                         [4, 0, 3, 4, 0, 4, 3, 4, 3, 2, 2, 2, 1, 4, 3, 4, 3, 0, 0, 1]]

        landscape.put_tile(outer, *outer_location)
        self.assertEqual(landscape.bushes, correct_outer)

    def test_el_tile(self):
        """Checks whether putting el shape tile have the desired result."""
        tp_input = Tile_input('../inputs/tilesproblem_1326658913086500.txt')
        landscape = Landscape(tp_input)

        el = next((x for x in landscape.tiles if x.type == 'EL_SHAPE'), None)
        el_location = (16, 16)
        correct_el = [[2, 2, 1, 3, 0, 3, 4, 0, 4, 2, 2, 4, 0, 4, 0, 0, 0, 2, 4, 3],
                      [0, 2, 1, 3, 2, 2, 0, 0, 0, 1, 0, 1, 2, 2, 0, 2, 3, 4, 4, 4],
                      [2, 1, 0, 0, 0, 2, 2, 4, 3, 2, 2, 2, 1, 2, 2, 0, 0, 1, 1, 0],
                      [0, 3, 2, 0, 1, 0, 1, 1, 4, 1, 3, 4, 2, 1, 0, 0, 0, 1, 4, 1],
                      [4, 2, 3, 4, 4, 4, 0, 2, 2, 0, 0, 3, 2, 3, 0, 2, 0, 2, 3, 2],
                      [2, 4, 1, 0, 1, 1, 1, 4, 1, 0, 1, 3, 0, 3, 2, 0, 4, 0, 1, 2],
                      [4, 3, 1, 4, 3, 3, 1, 4, 0, 1, 1, 1, 4, 2, 2, 4, 1, 4, 3, 4],
                      [2, 1, 1, 1, 4, 4, 3, 4, 4, 2, 0, 3, 0, 3, 0, 3, 4, 4, 0, 0],
                      [1, 0, 0, 3, 0, 3, 2, 2, 4, 3, 3, 2, 4, 0, 0, 0, 1, 4, 3, 0],
                      [0, 1, 3, 1, 3, 2, 3, 2, 1, 0, 0, 1, 4, 3, 2, 1, 2, 4, 1, 3],
                      [0, 3, 0, 2, 3, 4, 3, 3, 1, 0, 0, 1, 2, 3, 3, 0, 2, 1, 2, 3],
                      [1, 3, 1, 1, 4, 4, 4, 2, 0, 4, 4, 3, 4, 1, 1, 2, 2, 3, 2, 3],
                      [2, 1, 0, 1, 1, 1, 0, 1, 2, 1, 3, 2, 2, 3, 3, 4, 0, 0, 3, 4],
                      [4, 2, 0, 0, 2, 3, 2, 1, 1, 1, 4, 0, 4, 4, 3, 2, 2, 0, 2, 3],
                      [3, 1, 4, 3, 0, 1, 4, 4, 1, 1, 3, 1, 1, 1, 0, 0, 2, 1, 2, 0],
                      [3, 2, 2, 4, 3, 1, 1, 4, 1, 0, 0, 3, 1, 2, 3, 2, 2, 2, 3, 4],
                      [0, 2, 2, 1, 3, 3, 1, 1, 0, 0, 0, 3, 0, 4, 4, 2, 0, 0, 0, 0],
                      [0, 1, 4, 3, 0, 0, 1, 1, 3, 3, 0, 4, 3, 4, 4, 4, 0, 1, 1, 1],
                      [3, 2, 1, 2, 0, 3, 1, 1, 3, 4, 2, 4, 0, 3, 0, 2, 0, 0, 4, 1],
                      [4, 0, 3, 4, 0, 4, 3, 4, 3, 2, 2, 2, 1, 4, 3, 4, 0, 0, 0, 1]]

        landscape.put_tile(el, *el_location)
        self.assertEqual(landscape.bushes, correct_el)

    def test_full_tile(self):
        """Checks whether putting full shape tile have the desired result."""
        tp_input = Tile_input('../inputs/tilesproblem_1326658913086500.txt')
        landscape = Landscape(tp_input)

        full = next((x for x in landscape.tiles if x.type == 'FULL_BLOCK'), None)
        full_location = (12, 12)
        correct_full = [[2, 2, 1, 3, 0, 3, 4, 0, 4, 2, 2, 4, 0, 4, 0, 0, 0, 2, 4, 3],
                        [0, 2, 1, 3, 2, 2, 0, 0, 0, 1, 0, 1, 2, 2, 0, 2, 3, 4, 4, 4],
                        [2, 1, 0, 0, 0, 2, 2, 4, 3, 2, 2, 2, 1, 2, 2, 0, 0, 1, 1, 0],
                        [0, 3, 2, 0, 1, 0, 1, 1, 4, 1, 3, 4, 2, 1, 0, 0, 0, 1, 4, 1],
                        [4, 2, 3, 4, 4, 4, 0, 2, 2, 0, 0, 3, 2, 3, 0, 2, 0, 2, 3, 2],
                        [2, 4, 1, 0, 1, 1, 1, 4, 1, 0, 1, 3, 0, 3, 2, 0, 4, 0, 1, 2],
                        [4, 3, 1, 4, 3, 3, 1, 4, 0, 1, 1, 1, 4, 2, 2, 4, 1, 4, 3, 4],
                        [2, 1, 1, 1, 4, 4, 3, 4, 4, 2, 0, 3, 0, 3, 0, 3, 4, 4, 0, 0],
                        [1, 0, 0, 3, 0, 3, 2, 2, 4, 3, 3, 2, 4, 0, 0, 0, 1, 4, 3, 0],
                        [0, 1, 3, 1, 3, 2, 3, 2, 1, 0, 0, 1, 4, 3, 2, 1, 2, 4, 1, 3],
                        [0, 3, 0, 2, 3, 4, 3, 3, 1, 0, 0, 1, 2, 3, 3, 0, 2, 1, 2, 3],
                        [1, 3, 1, 1, 4, 4, 4, 2, 0, 4, 4, 3, 4, 1, 1, 2, 2, 3, 2, 3],
                        [2, 1, 0, 1, 1, 1, 0, 1, 2, 1, 3, 2, 0, 0, 0, 0, 0, 0, 3, 4],
                        [4, 2, 0, 0, 2, 3, 2, 1, 1, 1, 4, 0, 0, 0, 0, 0, 2, 0, 2, 3],
                        [3, 1, 4, 3, 0, 1, 4, 4, 1, 1, 3, 1, 0, 0, 0, 0, 2, 1, 2, 0],
                        [3, 2, 2, 4, 3, 1, 1, 4, 1, 0, 0, 3, 0, 0, 0, 0, 2, 2, 3, 4],
                        [0, 2, 2, 1, 3, 3, 1, 1, 0, 0, 0, 3, 0, 4, 4, 2, 2, 2, 4, 4],
                        [0, 1, 4, 3, 0, 0, 1, 1, 3, 3, 0, 4, 3, 4, 4, 4, 4, 1, 1, 1],
                        [3, 2, 1, 2, 0, 3, 1, 1, 3, 4, 2, 4, 0, 3, 0, 2, 0, 0, 4, 1],
                        [4, 0, 3, 4, 0, 4, 3, 4, 3, 2, 2, 2, 1, 4, 3, 4, 3, 0, 0, 1]]

        landscape.put_tile(full, *full_location)
        self.assertEqual(landscape.bushes, correct_full)


if __name__ == '__main__':
    unittest.main()