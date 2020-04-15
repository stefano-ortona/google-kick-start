from unittest import TestCase
from y2013.roundb.meet_party import find_best_point


class TestMeetParty(TestCase):

    def test_find_best_point_one_square(self):
        self.assertEqual([12, 1, 1], find_best_point([[0, 0, 2, 2]]))
        self.assertEqual([14880, 15, 15], find_best_point([[0, 0, 30, 30]]))
        self.assertEqual([13500, 14, 14], find_best_point([[0, 0, 29, 29]]))

    def test_find_best_point_single_point_square(self):
        self.assertEqual([6, -1, 2], find_best_point([[-1, 2, -1, 2], [0, 0, 0, 0], [1, 3, 1, 3]]))

    def test_find_best_point_two_squares(self):
        self.assertEqual([12, 1, 1], find_best_point([[0, 0, 2, 2]]))

    def test_find_best_point_six_squares(self):
        squares = [[468, 377, 468, 377], [839, -105, 839, -105], [-871, 487, -871, 487], [-307, 651, -307, 651],
                   [135, -929, 135, -929], [-411, -829, -411, -829], [745, -64, 745, -64], [336, 784, 336, 784],
                   [-875, -84, -875, -84], [-723, -736, -723, -736], [701, -818, 701, -818], [-239, 210, -239, 210],
                   [-15, 614, -15, 614], [362, 225, 362, 225], [894, 443, 894, 443], [-352, -303, -352, -303],
                   [-287, 254, -287, 255], [-739, -960, -739, -960], [110, 28, 110, 28], [540, 434, 541, 435],
                   [-103, -962, -102, -962], [913, -274, 913, -273], [835, -730, 836, -730], [544, 866, 545, 867],
                   [-97, -358, -96, -358], [-490, -319, -490, -319], [-122, 700, -122, 702], [37, 902, 39, 902],
                   [103, 266, 104, 266], [-581, -714, -579, -710]]
        self.assertEqual([62565, -97, -358], find_best_point(squares))
