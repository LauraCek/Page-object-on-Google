from selenium import webdriver
from selenium.webdriver.common.by import By
 
class Page(object):
	def __init__(self, driver):
		self.driver = driver
		self.timeout = 30

	def find_element(self, *locator):
		return self.driver.find_element(*locator)

	def open(self, url):
		self.driver.get(url)
