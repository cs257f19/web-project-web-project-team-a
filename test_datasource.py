import unittest
from datasource import *


class DataSourceTest(unittest.TestCase):

    def setUp(self) -> None:
        self.cq = courseQuery(None, None, None, None, None, 'QRE')

    def test_if_fulfills_QRE(self):
        req_str = 'QRE'
        self.assertTrue(req_str in self.cq.courseRequirements)

    def test_if_fulfills_LAA(self):
        req_str = 'LAA'
        self.assertTrue(req_str in self.cq.courseRequirements)

    def test_if_fulfills_HUM(self):
        req_str = 'HUM'
        self.assertTrue(req_str in self.cq.courseRequirements)

    def test_if_input_is_str(self):
        req_type = str
        self.assertTrue(req_type == type(self.cq.courseRequirements))


if __name__ == '__main__':
    unittest.main()
