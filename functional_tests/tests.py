from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
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
class NewVisitorTest(LiveServerTestCase):
	
	def setUp(self):
		# Client opens browser
		self.browser = webdriver.Firefox()
		# Wait for load
		self.browser.implicitly_wait(3)

	def tearDown(self):
		# Client closes browser
		self.browser.quit()
    
	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(row_text in [row.text for row in rows], 'New to-do item did not appear in table - text was:\n%s' % (table.text))

	def test_can_start_a_list_and_retrieve_it_later(self):
		# Client navigates to site
		self.browser.get(self.live_server_url)
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

		# A new URL is generated for user
		edith_list_url = self.browser.current_url
		self.assertRegex(edith_list_url, '/lists/.+')
		# Page updates and lists user's entry
		# At least one of the rows of table should match user's latest entry
		self.check_for_row_in_list_table('1: Buy peacock feathers')

		# Enters another item
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)

		# Page updates again and lists second entry with appropriate numbering
		self.check_for_row_in_list_table('1: Buy peacock feathers')
		self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

		# A new user, Francis, now visits the site
        
		## A new browser session is used to ensure that no information is being passed through cookies etc
		self.browser.quit()
		self.browser = webdriver.Firefox()

		# Francis visits the site
		self.browser.get(self.live_server_url)

		# Francis should not be able to see previous user's information
		page_text = self.browser.get_element_by_tag_name('body').text
		self.assertNotIn('Buy peacock feathers', page_text)
		self.assertNotIn('make a fly', page_text)

		# Francis enters his own To-Do list
		inputbox = self.browser.find_element_by_id('id_new_item')
		# He enters his item
		inputbox.send_keys('Buy milk')
		inputbox.send_keys(Keys.ENTER)

		# A new URL is generated for him    
		francis_list_url = self.browser.current_url
		self.assertRegex(francis_list_url, '/lists/.+')
		# The URL is unique to him
		self.assertNotEqual(francis_list_url, edith_list_url)
        
		# Again, previous user's content should not appear
		page_text = self.browser.get_element_by_tag_name('body').text
		self.assertNotIn('Buy peacock feathers', page_text)
		self.assertNotIn('make a fly', page_text)

		# His own content should appear
		self.assertIn('Buy milk', page_text)

        
		self.fail("Finish the Test!")


