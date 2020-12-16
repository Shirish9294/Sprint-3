import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

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

        driver.get("http://127.0.0.1:8000/logout")
        time.sleep(2)

        user = "Test01"
        pwd = "ABC@1234"

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

        driver.get("http://127.0.0.1:8000")
        time.sleep(2)
        try:
            elem = driver.find_element_by_xpath("/html/body/header/div[1]/div/div[2]/a[1]")
            assert True

        except NoSuchElementException:
            self.fail("Login Failed - user may not exist")
            assert False

        time.sleep(3)

        try:
            elem = driver.find_element_by_xpath("/html/body/header/div[1]/div/div[2]/a[1]").click()
            assert True
            time.sleep(3)
        except NoSuchElementException:
            self.fail("User Profile is not displayed")
            assert False
            time.sleep(1)
        except:
            self.fail("User Profile does not exist")
            assert False
            time.sleep(1)

        time.sleep(3)

        # driver.get("http://127.0.0.1:8000/user")
        # elem = driver.find_element_by_id("id_username")
        # elem.send_keys(user)
        # elem = driver.find_element_by_id("id_password")
        # elem.send_keys(pwd)
        # elem.send_keys(Keys.RETURN)
        # driver.get("http://127.0.0.1:8000/user")
        assert "Logged In"
        time.sleep(3)

        elem = driver.find_element_by_xpath("/html/body/header/div[1]/div/div[2]/a[1]").click()
        time.sleep(3)
        continue_test = False

        try:
            elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/table/tbody/tr[1]/th/a[1]").click()
            continue_test = True

        except NoSuchElementException:
            self.fail("User Profile Update not successful")
            assert False
            time.sleep(1)
        except:
            self.fail("User Profile Update does not exist. ")
            assert False
            time.sleep(1)

        if continue_test:
            elem = driver.find_element_by_id("id_phone")
            elem.send_keys("4444444444")
            elem = driver.find_element_by_id("id_address")
            elem.send_keys("123 ABC ")
            elem = driver.find_element_by_id("id_city")
            elem.send_keys("Omaha")
            elem = driver.find_element_by_id("id_state")
            elem.send_keys("Nebraska")
            elem = driver.find_element_by_id("id_country")
            elem.send_keys("United States")
            time.sleep(6)
            elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/form/div/button").click()
            time.sleep(6)

        driver.get("http://127.0.0.1:8000")
        time.sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
