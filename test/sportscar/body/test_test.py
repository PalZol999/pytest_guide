from pytest import mark 
from selenium import webdriver

@mark.ui
class BodyTest:
    def test_can_navigate_to_page(self):  
        browser = webdriver.Chrome()
        browser.get('https://www.motortrend.com/')
        assert True

