from pytest import mark 

@mark.failed
class BodyTests:
    @mark.ui
    def test_can_navigate_to_page(self, chrome_browser):  
        chrome_browser.get('https://www.motortrend.com/')
        assert True

    @mark.skip(reason= "not yet updat")
    def test_bumper(self):
        assert True
    
    @mark.xfail(reason= "to be deprecated")
    def test_windshield(self):
        assert False
