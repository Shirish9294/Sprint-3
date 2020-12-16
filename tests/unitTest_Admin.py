import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class Apparel360_SignUp(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_cms(self):
        user = "diksha"
        pwd = "Diksha@1998"

        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(5)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000/admin")
        continue_test = True
        time.sleep(3)

        driver.get("http://127.0.0.1:8000/admin/auth/user")
        time.sleep (2)
        driver.get("http://127.0.0.1:8000/admin/auth/user/add")
        continue_test = True
        time.sleep(3)
        if continue_test:
            elem = driver.find_element_by_id("id_username")
            elem.send_keys("testing")
            elem = driver.find_element_by_id("id_password1")
            elem.send_keys("ABC@1234567")
            elem = driver.find_element_by_id("id_password2")
            elem.send_keys("ABC@1234567")
            elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/div/form/div/div/input[1]").click()
            time.sleep(3)
            elem = driver.find_element_by_id("id_first_name")
            elem.send_keys("ABC")
            elem = driver.find_element_by_id("id_last_name")
            elem.send_keys("DEF")
            elem = driver.find_element_by_id("id_email")
            elem.send_keys("abc@gmail.com")
            time.sleep(3)
            elem = driver.find_element_by_xpath("//*[@id='user_form']/div/div/input[1]").click()
            time.sleep(9)

        driver.get("http://127.0.0.1:8000/admin/auth/user")
        elem = driver.find_element_by_xpath("//*[@id='result_list']/tbody/tr[7]/th/a").click()
        time.sleep(1)
        elem = driver.find_element_by_xpath("//*[@id='user_form']/div/div/p/a").click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("//*[@id='content']/form/div/input[2]").click()
        time.sleep(2)

        driver.get("http://127.0.0.1:8000/admin/auth/user")
        driver.get("http://127.0.0.1:8000/admin")
        time.sleep(4)


        driver.get("http://127.0.0.1:8000/admin/coupons/coupon")
        time.sleep(2)
        driver.get("http://127.0.0.1:8000/admin/coupons/coupon/add")
        continue_test = True
        time.sleep(2)
        if continue_test:
            elem = driver.find_element_by_id("id_code")
            elem.send_keys("December2020")
            elem = driver.find_element_by_id("id_valid_from_0")
            elem.send_keys("2020-12-15")
            elem = driver.find_element_by_id("id_valid_from_1")
            elem.send_keys("13:20:45")
            time.sleep(3)
            elem = driver.find_element_by_id("id_valid_to_0")
            elem.send_keys("2020-12-30")
            elem = driver.find_element_by_id("id_valid_to_1")
            elem.send_keys("13:20:45")
            elem = driver.find_element_by_id("id_discount")
            elem.send_keys("10")
            elem = driver.find_element_by_id("id_active").click()
            elem = driver.find_element_by_xpath("//*[@id='coupon_form']/div/div/input[1]").click()
        time.sleep(10)

        driver.get("http://127.0.0.1:8000/admin/coupons/coupon")
        elem = driver.find_element_by_xpath("//*[@id='result_list']/tbody/tr[1]/th/a").click()
        time.sleep(1)
        elem = driver.find_element_by_xpath("//*[@id='coupon_form']/div/div/p/a").click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("//*[@id='content']/form/div/input[2]").click()
        time.sleep(2)


        driver.get("http://127.0.0.1:8000/admin/coupons/coupon")
        driver.get("http://127.0.0.1:8000/admin")
        time.sleep(4)

        driver.get("http://127.0.0.1:8000/admin/product/category")
        time.sleep(2)
        driver.get("http://127.0.0.1:8000/admin/product/category/add")
        continue_test = True
        time.sleep(1)
        if continue_test:
              elem = driver.find_element_by_id("id_name")
              elem.send_keys("Jeans")
        elem = driver.find_element_by_xpath("//*[@id='category_form']/div/div/input[1]").click()
        time.sleep(4)

        driver.get("http://127.0.0.1:8000/admin/product/category")
        elem = driver.find_element_by_xpath("//*[@id='result_list']/tbody/tr[1]/th/a").click()
        time.sleep(1)
        elem = driver.find_element_by_xpath("//*[@id='category_form']/div/div/p/a").click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("//*[@id='content']/form/div/input[2]").click()
        time.sleep(2)

        driver.get("http://127.0.0.1:8000/admin/product/category")
        driver.get("http://127.0.0.1:8000/admin")
        time.sleep(5)

        # driver.get("http://127.0.0.1:8000/admin/product/product")
        # time.sleep(2)
        # driver.get("http://127.0.0.1:8000/admin/product/product/add")
        # continue_test = True
        # time.sleep(2)
        # if continue_test:
        #       elem = driver.find_element_by_id("id_category").select()
        #       elem.selectByVisibleTest("Sweaters") ;
        #       elem = driver.find_element_by_id("id_name")
        #       elem.send_keys("Womens Turtleneck Sweater")
        #       elem = driver.find_element_by_id("id_slug")
        #       elem.send_keys("sweater")
        #       elem = driver.find_element_by_id("id_description")
        #       elem.send_keys("45% Viscose, 35% Nylon, 20% Polyester")
        #       elem = driver.find_element_by_id("id_price")
        #       elem.send_keys("35")
        # elem = driver.find_element_by_xpath("//*[@id='product_form']/div/div/input[1]").click()
        # time.sleep(4)
        #
        # driver.get("http://127.0.0.1:8000/admin/product/product")
        # driver.get("http://127.0.0.1:8000/admin")
        # time.sleep(5)
        

    def tearDown(self):
        self.driver.close()
if __name__ == '__main__':
    unittest.main()
