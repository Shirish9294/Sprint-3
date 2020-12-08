import unittest
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class CMS_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_cms(self):
        #login from the admin pane
        user = "ID"
        pwd = "PWD"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/user")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000/user")
        assert "Logged In"
        time.sleep(5)

        # find the ‘+ New’ and click it
        elem = driver.find_element_by_xpath("/html/body/header/div[1]/div/div[2]/a[1]").click()
        time.sleep(5)
        continue_test = False

        try:
            # verify New Client exists on new screen after clicking "+ New" button
            elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/table/tbody/tr[1]/th/a[1]").click()
            continue_test = True

        except NoSuchElementException:
            self.fail("Add new client does not appear = New Client button not present")
            assert False
            time.sleep(1)
        except:
            self.fail("Edit post NOT successful - error occurred: ")
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
    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
