from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:   # open site
    driver.get('https://telranedu.web.app/login')
# find by tag_name
    div = driver.find_element(By.TAG_NAME, 'div')
    div_1 = driver.find_element(By.CSS_SELECTOR, 'div')

    h1 = driver.find_element(By.TAG_NAME,'h1')
    h1_1 = driver.find_element(By.CSS_SELECTOR, 'h1')

    input = driver.find_element(By.TAG_NAME, 'input')
    input_1 = driver.find_element(By.CSS_SELECTOR, 'input')

    a_list = driver.find_elements(By.TAG_NAME,'a')
    a_list_1 = driver.find_elements(By.CSS_SELECTOR, 'a')
    print(len(a_list))

# by class
    container = driver.find_element(By.CLASS_NAME, 'container')
    container_1 = driver.find_element(By.CSS_SELECTOR, '.container') # с точкой

    navbar = driver.find_element(By.CLASS_NAME, 'navbar-component_nav__1X_4m')
    navbar_1 = driver.find_element(By.CSS_SELECTOR, '.navbar-component_nav__1X_4m') #с (.)

    login_login = driver.find_element(By.CLASS_NAME, 'login_login__3EHKB')
    login_login_1 = driver.find_element(By.CSS_SELECTOR, '.login_login__3EHKB') #(.)

# by ID

    root = driver.find_element(By.ID, 'root')
    root_1 = driver.find_element(By.CSS_SELECTOR, '#root')

    root_2 = driver.find_elements(By.ID, 'root')
    root_3 = driver.find_elements(By.CSS_SELECTOR, '#root')














finally:
    driver.quit()