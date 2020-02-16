from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get('http://www.pythonparatodos.com.br')
print(driver.current_url)
driver.get('http://www.pythonparatodos.com.br/cursos')
sleep(3)
driver.back()
sleep(3)
driver.forward()
sleep(2)
driver.refresh()
driver.save_screenshot('teste.png')
driver.close()

