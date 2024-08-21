from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_cart_button(browser):
    browser.get(link)
    time.sleep(30)
    add_to_basket = browser.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket").text
    assert add_to_basket in ["Добавить в корзину", "Add to basket", "Añadir al carrito", "Ajouter au panier"], f"Текст у кнопки должен быть: {add_to_basket}"

