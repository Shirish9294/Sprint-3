import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class Apparel360_Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_cms(self):
        user = "ID"
        pwd = "PWD"

        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/login")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(5)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        time.sleep(3)
        try:
           elem = driver.find_element_by_xpath("/html/body/header/div[1]/div/div[2]/a[1]")
           assert True

        except NoSuchElementException:
            self.fail("Login Failed - user may not exist")
            assert False

        time.sleep(3)

def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()


