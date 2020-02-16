from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://localhost:8000/ejemplo1.php')
driver.execute_script('window.alert("Script ejecutado")')

