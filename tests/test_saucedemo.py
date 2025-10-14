import pytest
import sys
import os
from selenium.webdriver.common.by import By
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from utils.helpers import login_saucedemo, get_driver



@pytest.fixture(scope="session")
def driver():
    #configuracion para consultar a selenium web driver
    driver = get_driver()
    yield driver
    driver.quit()

def test_login(driver):

    login_saucedemo(driver)
    assert "/inventory.html" in driver.current_url
    titulo = driver.find_element(By.CSS_SELECTOR, "div.header_secondary_container .title").text
    assert titulo == "Products"
    #logueo de usuarios con username y password
    #click al boton de login
    #redirigir a la pagina de inventario
    #verificar el titulo de pagina, inventory


def test_catalogo(driver):
    login_saucedemo(driver)

    products = driver.find_elements(By.CLASS_NAME, "inventory_list")
    assert len(products) > 0
    #logueo de usuarios con username y password
    #click al boton de login
    #verificar el titulo pero del html
    #comprobar si existen productos visibles en la pagina (len())
    #verificar elementos imp de la pagina

def test_carrito(driver):
    login_saucedemo(driver)
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    total_products = len(products)

    if total_products >= 2:
        products[0].find_element(By.TAG_NAME, "button").click()
        products[1].find_element(By.TAG_NAME, "button").click()

        badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert badge == "2"

    
    #logueo de usuarios con username y password
    #click al boton de login
    #llevarme a la pagina del carrito de compra
    #incremento del carrito a agregar un producto
    #comprobar que el carrito aparezca el producto correctamente
