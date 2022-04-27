from selenium.webdriver.common.by import By
import time

def test_guest_should_see_add_to_cart_btn(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    add_to_cart_btn = len(browser.find_elements(By.XPATH, "//button[contains(@class, 'btn-add-to-basket')]"))
    assert add_to_cart_btn > 0, "button is not found"
