from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get('http://localhost:8000/ejemplo1.php')

nombre = driver.find_element_by_name('nombre')
email = driver.find_element_by_name('email')
telefono = driver.find_element_by_name('telefono')
enviar = driver.find_element_by_name('enviar')

nombre.send_keys('Yuri x Code')
email.send_keys('mail@yurixcode.com')
telefono.send_keys('+34 622 115 301')

enviar.click()
print(driver.page_source)
driver.close()

