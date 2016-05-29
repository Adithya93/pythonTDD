from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


'''
# Client opens browser
browser = webdriver.Firefox()

# Client navigates to site
browser.get("http://localhost:8000")

# Client sees To-Do List in page title
assert 'To-Do' in browser.title

# Client closes browser
browser.quit()
'''
class NewVisitorTest(unittest.TestCase):
	
	def setUp(self):
		# Client opens browser
		self.browser = webdriver.Firefox()
		# Wait for load
		self.browser.implicitly_wait(3)

	def tearDown(self):
		# Client closes browser
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# Client navigates to site
		self.browser.get("http://localhost:8000")
		# Client sees To-Do List in page title
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)
		
		# User is about to enter a new list item
		inputbox = self.browser.find_element_by_id('id_new_item')
		# Appropriate prompt is displayed to the user
		self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')
		# User enters his item
		inputbox.send_keys('Buy peacock feathers')
		# User hits enter
		inputbox.send_keys(Keys.ENTER)
		# Page updates and lists user's entry
		table = self.browser.find_element_by_id('id_list_table')
		# At least one of the rows of table should match user's latest entry
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(any(row.text == '1: Buy peacock feathers' for row in rows), 'New to-do item did not appear in table')

		# Enters more items which appear upon hitting enter.... <TO-DO>

		self.fail("Finish the Test!")

if __name__ == '__main__':
	unittest.main(warnings='ignore')




