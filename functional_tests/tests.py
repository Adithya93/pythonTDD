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

		#import time
		#time.sleep(10)
        
        # Page updates and lists user's entry
		#table = self.browser.find_element_by_id('id_list_table')
		
        # At least one of the rows of table should match user's latest entry
		#rows = table.find_elements_by_tag_name('tr')
		#self.assertTrue(any(row.text == '1: Buy peacock feathers' for row in rows), 'New to-do item did not appear in table - text was:\n%s' % (table.text))
		#self.assertIn('1: Buy peacock feathers', [row.text for row in rows])

		#self.assertTrue(self.check_for_row_in_list_table('1: Buy peacock feathers'), 'New to-do item did not appear in table - text was:\n%s' % (table.text))
		self.check_for_row_in_list_table('1: Buy peacock feathers')

		# Enters another item
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)

		# Page updates again and lists second entry with appropriate numbering
		#table = self.browser.find_element_by_id('id_list_table')
		#rows = table.find_elements_by_tag_name('tr')
		#self.assertIn('2: Use peacock feathers to make a fly', [row.text for row in rows])
		#self.assertTrue(self.check_for_row_in_list_table('1: Buy peacock feathers'), 'New to-do item did not appear in table - text was:\n%s' % (table.text))
		self.check_for_row_in_list_table('1: Buy peacock feathers')
        #self.assertTrue(self.check_for_row_in_list_table('2: Use peacock feathers to make a fly'), 'New to-do item did not appear in table - text was:\n%s' % (table.text))
		self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

		self.fail("Finish the Test!")


