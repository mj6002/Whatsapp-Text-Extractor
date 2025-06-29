#******* SELENIUM TO WRITE TEST *******
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

'''
The test case class is inherited from unittest.TestCase. 
Inheriting from the TestCase class is the way to tell unittest 
module that this is a test case:
'''
class PythonOrgSearch(unittest.TestCase):

    '''
    The setUp method is part of initialization. This method will get 
    called before every test function which you are going to write in 
    this test case class. Here you are creating an instance of a 
    Chrome WebDriver.
    '''
    def setUp(self):
        path = "D:/UniqueDressup/chromedriver-win64/chromedriver.exe"
        serv = Service(executable_path = path)
        self.driver = webdriver.Chrome(service=serv)

    '''
    This is the test case method. The test case method should always 
    start with characters test. The first line inside this method 
    creates a local reference to the driver object created in setUp 
    method.
    '''
    def test_serach_in_python_org(self):
        driver = self.driver

        '''
        The driver.get method will navigate to a page given by the URL. 
        WebDriver will wait until the page has fully loaded (that is, the 
        “onload” event has fired) before returning control to your test or 
        script. 
        '''
        driver.get("http://www.python.org")

        '''
        The next line is an assertion to confirm that title has the word "Python in it:"
        '''
        self.assertIn("Python", driver.title)

        '''
        WebDriver offers a number of ways to find elements using the 
        find_element method. For example, the input text element can be 
        located by its name attribute using the find_element method.
        '''
        elem = driver.find_element(By.NAME, "q")

        '''
        Next, we are sending keys, this is similar to entering keys 
        using your keyboard. Special keys can be sent using the Keys 
        class imported from selenium.webdriver.common.keys:
        '''
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)

        '''
        After submission of the page, you should get the result as per 
        search if there is any. To ensure that some results are found, 
        make an assertion:
        '''
        self.assertNotIn("No result found", driver.page_source)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)