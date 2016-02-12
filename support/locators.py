from selenium.webdriver.common.by import By

class GooglePageLocators(object):
	search_field = (By.ID, 'lst-ib')
	search_button = (By.NAME, 'btnG')