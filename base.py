from __future__ import unicode_literals

import unittest


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_pass(self):
        self.assertTrue(True)

    def test_fail(self):
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
