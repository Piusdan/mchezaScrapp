from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_site(arg):
    url = 'http://www.mcheza.co.ke/sports'
    driver = webdriver.Firefox()
    driver.get(url)
    try:
        element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, arg)))
    except:
        print("Connection unsuccesfull")

    return (driver.find_elements_by_class_name(arg))
