from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
# Actions
class actions_class:

    # Constructor.
    def __init__(self, driver):
        self.driver = driver

    # Open the page with the link.
    def load_page(self, selector):
        self.driver.get(selector)   

    # Get the title of the page and return it.
    def get_title_of_the_page(self):
        return self.driver.title

    # Method to click / select a button / option on the page.
    def click_btn(self, selector, timeout = 30):
        wait = WebDriverWait(self.driver,timeout)
        btn = wait.until(ec.visibility_of_element_located(selector))
        btn.click()