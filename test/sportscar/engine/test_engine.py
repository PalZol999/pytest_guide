from pytest import mark  # terminal: pytest -m engine 


@mark.ui
@mark.smoke
@mark.engine # terminal: pytest -m "engine or body" 
def test_can_navigate_to_engine_page(chrome_browser):
    chrome_browser.get("https://www.artofmanliness.com/")
    assert True