from selenium import webdriver
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
		self.fail("Finish the Test!")

if __name__ == '__main__':
	unittest.main(warnings='ignore')




