from pages.actions import actions_class
import pages.page_objects as page_object

# Test

def test_practice_page(browser):

    driver = actions_class(browser)
    driver.load_page(page_object.URL)