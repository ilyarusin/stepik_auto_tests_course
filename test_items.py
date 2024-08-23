from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_cart_button(browser):
    browser.get(link)
    time.sleep(10)
    add_to_basket = browser.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    assert add_to_basket.is_displayed(), f"Кнопка {add_to_basket} отсутствует"

