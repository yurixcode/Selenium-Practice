from selenium import webdriver

def esperar(driver):
    while True:
        try:
            if driver.find_element_by_id("enviar"):
                print(driver.find_element_by_id("enviar").get_attribute('value'))
                driver.close()
                return
                
        except:
            print('Error')

if __name__ == "__main__":
    print('Inicio')
    driver = webdriver.Firefox()

    driver.get('http://localhost:8000/ejemplo2.php')
    esperar(driver)

    driver.close()

    print('Final')
