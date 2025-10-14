from selenium import webdriver
from selenium.webdriver.common.by import By #LLAMAR A LOS SELECTORES
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys #PASAR LOS DATOS
from selenium.webdriver.chrome.service import Service
import time

URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

def get_driver():
    driver =webdriver.Chrome()
    time.sleep(3)
    return driver


def login_saucedemo(driver):
    driver.get(URL)

    time.sleep(3)
    #INGRESAR LAS CREDENCIALES
    driver.find_element(By.NAME, "user-name").send_keys(USERNAME)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()
    
    time.sleep(3)


