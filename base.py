from __future__ import unicode_literals

import unittest

from selenium import webdriver


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.close()

    def test_interact_form(self):
        self.driver.get(
            'https://www.w3schools.com/html/html_form_elements.asp')
        field = self.driver.find_element_by_css_selector('#main > textarea')
        # field = self.driver.find_element_by_xpath('//*[@id="main"]/textarea')
        field.send_keys('search here')
        # field.send_keys(Keys.ENTER)

    def test_interact_options(self):
        self.driver.get(
            'https://channelfix.com/#ranking')
        # iterate all options
        select = self.driver.find_element_by_class_name('categories')
        options = select.find_elements_by_tag_name('option')
        for option in options:
            print option.get_attribute('value')


if __name__ == '__main__':
    unittest.main()
