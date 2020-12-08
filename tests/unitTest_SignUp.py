import unittest
import time
from selenium import webdriver


class Apparel360_SignUp(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_cms(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/signup")
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/header/div[1]/div/div[2]/a[2]")
        continue_test = True
        time.sleep(3)

        if continue_test:
            elem = driver.find_element_by_id("id_username")
            elem.send_keys("Test01")
            elem = driver.find_element_by_id("id_email")
            elem.send_keys("test01@gmail.com")
            elem = driver.find_element_by_id("id_first_name")
            elem.send_keys("Test")
            elem = driver.find_element_by_id("id_last_name")
            elem.send_keys("Test")
            elem = driver.find_element_by_id("id_password1")
            elem.send_keys("ABC@1234")
            elem = driver.find_element_by_id("id_password2")
            elem.send_keys("ABC@1234")
            time.sleep(6)
            elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/form/div/button").click()
            time.sleep(6)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
