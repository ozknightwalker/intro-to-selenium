from __future__ import unicode_literals

import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# or use Chrome, PhantomJS, or any webdriver you provided given that selenium
# supports the provided driver
driver = webdriver.Firefox()  # or Firefox('path of the driver')

driver.get('https://google.com')
# do the magic here
field = driver.find_element_by_name('q')
field.send_keys('search something here!')
field.send_keys(Keys.ENTER)

# get page source
driver.page_source

# don't forget to close the browser after the execution
driver.close()


# class BaseTestCase(unittest.TestCase):

#     def setUp(self):
#         self.driver = webdriver.Firefox()

#     def tearDown(self):
#         self.driver.close()

#     def test_google_search(self):
#         self.driver.get('http://google.com')
#         field = self.driver.find_element_by_name('q')
#         field.send_keys('search here')
#         field.send_keys(Keys.ENTER)
#         import time
#         time.sleep(1)
#         self.assertIn('search here', self.driver.title)


# if __name__ == '__main__':
#     unittest.main()
