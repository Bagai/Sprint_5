from selenium.common.exceptions import NoSuchElementException

def is_element_present(webdriver, xpath):
    try:
        webdriver.find_element(*xpath)
    except NoSuchElementException:
        return False
    return True
