from support.base import Page
from support.locators import *


class GooglePage(Page):
	def search_for_something(self, text):
		self.driver.find_element(*GooglePageLocators.search_field).send_keys(text)
		self.driver.find_element(*GooglePageLocators.search_button).click()
