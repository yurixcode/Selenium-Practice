from selenium import webdriver

print('Inicio')
driver = webdriver.Firefox()

driver.get('http://localhost:8000/ejemplo2.php')
print(driver.find_element_by_id('enviar').get_attribute('value'))

driver.close()

print('Final')