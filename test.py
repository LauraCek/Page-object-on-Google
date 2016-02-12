import unittest
from selenium import webdriver
from pages.main_page import *

class GoogleTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		#self.driver.get('http://www.google.com')

	def test_search(self):
		main_page = GooglePage(self.driver)
		main_page.open('http://www.google.com')
		main_page.search_for_something('ISTQB')



