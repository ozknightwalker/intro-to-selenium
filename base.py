from __future__ import unicode_literals

import unittest

from selenium import webdriver


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ setUpClass is called before all test runs """
        super(BaseTestCase, cls).setUpClass()
        cls.driver = webdriver.Firefox()

    @classmethod
    def tearDownClass(cls):
        """ tearDownClass is called when all test are done """
        cls.driver.close()
        super(BaseTestCase, cls).tearDownClass()

    def setUp(self):
        """ setUp runs when every start of every test """
        pass

    def tearDown(self):
        """ tearDown run at the end of every test """
        pass

    def test_interact_form(self):
        self.driver.get(
            'https://www.w3schools.com/html/html_form_elements.asp')
        field = self.driver.find_element_by_css_selector('#main > textarea')
        # field = self.driver.find_element_by_xpath('//*[@id="main"]/textarea')
        field.send_keys('search here')
        # field.send_keys(Keys.ENTER)

    def test_interact_options(self):
        self.driver.get('https://channelfix.com/#ranking')
        # iterate all options
        select = self.driver.find_element_by_class_name('categories')
        options = select.find_elements_by_tag_name('option')
        for option in options:
            print option.get_attribute('value')


if __name__ == '__main__':
    unittest.main()
