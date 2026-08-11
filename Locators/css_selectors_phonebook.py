# open browser
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# open site
try:
    driver.get('https://telranedu.web.app/login')

# by tag_name
    div = driver.find_element(By.TAG_NAME, 'div')
    div_1 = driver.find_element(By.CSS_SELECTOR, 'div')
    div_2 = driver.find_element(By.XPATH, '//div')

    a = driver.find_element(By.TAG_NAME, 'a')
    a_1 = driver.find_element(By.CSS_SELECTOR, 'a')
    a_2 = driver.find_element(By.XPATH, '//a')


#by class

    container = driver.find_element(By.CLASS_NAME, 'container')
    container_1 = driver.find_element(By.CSS_SELECTOR, '.container')
    container_2 = driver.find_element(By.XPATH, "//div[@class='container']")

    navbar = driver.find_element(By.CLASS_NAME, 'navbar-component_nav__1X_4m')
    navbar_1 = driver.find_element(By.CSS_SELECTOR, '.navbar-component_nav__1X_4m')
    navbar_2 = driver.find_element(By.XPATH, "//*[@class ='navbar-component_nav__1X_4m']")

#by id

    root = driver.find_element(By.ID, 'root')
    root_1 = driver.find_element(By.CSS_SELECTOR, '#root')
    root_2 = driver.find_element(By.XPATH, "//*[@id='root']")

finally:
    driver.quit()