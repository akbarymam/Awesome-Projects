from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains 
from time import sleep

class Testing:
	def __init__(self):
		self.browser = webdriver.Firefox()
		self.browser.get('http://127.0.0.1:5000')
		self.current = 'Prediction'
		self.result = {}
		sleep(2)

	def page(self, arg):
		try:
			if self.current != arg:
				self.current = arg
				self.browser.find_element_by_link_text(arg).click()
		except:
			self.result['Page'] = "Page didn't load successfully"
	
	def prediction_test(self, a, b, c, d, e, f, check):
		self.page('Prediction')
		sleep(2)
		Select(self.browser.find_element_by_id('buying')).select_by_visible_text(a)
		Select(self.browser.find_element_by_id('maintainence')).select_by_visible_text(b)
		Select(self.browser.find_element_by_id('doors')).select_by_visible_text(c)
		Select(self.browser.find_element_by_id('persons')).select_by_visible_text(d)
		Select(self.browser.find_element_by_id('lug_boot')).select_by_visible_text(e)
		Select(self.browser.find_element_by_id('safety')).select_by_visible_text(f)
		self.browser.find_element_by_tag_name('button').click()
		try:
			assert check in self.browser.find_element_by_xpath('//b//h3').text
			self.result[check] = 'Appropriate Result Received'
		except AssertionError:
			self.result[check] = 'Unexpected or No Result Received'

	def accuracy_test(self):
		sleep(2)
		try:
			assert float(self.browser.find_element_by_class_name('bg-primary').text[-6:-1])
			self.result['Accuracy'] = 'Valid Accuracy Value'
		except AssertionError:
			self.result['Accuracy'] = 'Invalid Accuracy Value'
	
	def classification_test(self):
		self.page('Classification')
		action = ActionChains(self.browser)
		sleep(2)
		flipper_before =self.browser.find_element_by_class_name('flipper').value_of_css_property('transform')
		action.move_to_element(self.browser.find_element_by_class_name('flip-container')).perform()
		flipper_after = self.browser.find_element_by_class_name('flipper').value_of_css_property('transform')
		try:
			assert flipper_before != flipper_after
			self.result['Flipping'] = 'Flipping Successful'
		except AssertionError:
			self.result['Flipping'] = 'Flipping Unsuccessful'
	
	def unit_test(self):
		self.page('Testing')
		sleep(2)
		self.browser.find_element_by_xpath('//button[@onclick="test(false);"]').click()
		self.result['Unit Testing'] = 'Performed'
		
	def quit(self):
		sleep(2)
		self.browser.quit()
		return self.result
