from __future__ import unicode_literals

import unittest


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpTestData(self):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
