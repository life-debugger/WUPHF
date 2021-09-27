import time

from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

USERNAME = 'toutounchi.ma'
PASSWORD = 'lilythebrave'

if __name__ == '__main__':
    options = Options()
    options.add_argument("--disable-notifications")
    # options.add_argument('headless')
    options.add_argument('--silent')
    driver = webdriver.Chrome(options=options)
    driver.get("http://www.instagram.com")

    # Accept the cookies
    try:
        elem = driver.find_element_by_class_name("bIiDR")
        elem.click()
    except Exception as e:
        print('There was no cookie popup')

    # Find username and password inputs
    time.sleep(5)
    inputs = driver.find_elements_by_class_name('_2hvTZ')
    inputs[0].send_keys(USERNAME)
    inputs[1].send_keys(PASSWORD)
    time.sleep(3)
    inputs[1].send_keys(Keys.RETURN)

    time.sleep(3)
    saveInfoBtn = driver.find_element_by_class_name('L3NKy')
    saveInfoBtn.click()

    try:
        time.sleep(2)
        allowNotifiBtn = driver.find_element_by_class_name('bIiDR')
        allowNotifiBtn.click()
    except Exception as e:
        print('no notification popup')

    time.sleep(2)
    driver.get('https://www.instagram.com/direct/new/')
    driver.find_element_by_name('queryBox').send_keys('billie')
    time.sleep(5)
    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    driver.find_element_by_class_name('rIacr').click()
    time.sleep(2)
    ta = driver.find_element_by_tag_name('textarea')
    ta.send_keys('How are you?')
    ta.send_keys(Keys.ENTER)
