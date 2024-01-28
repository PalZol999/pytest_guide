from pytest import mark 


def test_television_turns_on(tv_brand):
    print(f"{tv_brand} turns on as expected")

@mark.tv
def test_browser_can_navigate_to_train(browser):
    browser.get('https://techstepacademy.com/training-ground')