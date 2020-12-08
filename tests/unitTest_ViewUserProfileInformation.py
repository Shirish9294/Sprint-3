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

        try:
            # verify New Client exists on new screen after clicking "+ New" button
            elem = driver.find_element_by_xpath("/html/body/header/div[1]/div/div[2]/a[1]").click()
            assert True
            time.sleep (3)
        except NoSuchElementException:
            self.fail("Add new client does not appear = New Client button not present")
            assert False
            time.sleep(1)
        except:
            self.fail("Edit post NOT successful - error occurred: ")
            assert False
            time.sleep(1)

        time.sleep(3)

def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()