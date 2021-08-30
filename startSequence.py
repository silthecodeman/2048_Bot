import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

def initiate():
    pathelem = [i for i in os.getcwd()[1:].split('/')]
    path = '/{}/{}/Documents/geckodrivermac/chromedriver'.format(pathelem[0], pathelem[1])
    driver = webdriver.Chrome(executable_path=r'{}'.format(path))
    #driver.get('chrome://new-tab-page/')
    driver.get('https://play2048.co')
    print(2048)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'ezmobfooter')))
    driver.execute_script("document.getElementById('ezmobfooter').style.display='none';")

    return driver

def complete(driver):
    driver.quit()