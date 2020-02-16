from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://localhost:8000/ejemplo1.php')

obj = driver.find_element_by_id('enviar')

print('Texto del botón:', obj.get_attribute('value'))

driver.close()