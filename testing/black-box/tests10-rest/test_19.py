from selenium import webdriver
import time
driver = webdriver.Firefox(executable_path=r'/home/tarun/Desktop/testing/geckodriver-v0.25.0-linux64/geckodriver')
print("Test 19: View music files")
driver.get("http://localhost:8000/fs/home/tarun/Desktop/testing/black-box/tests10-rest")
time.sleep(3)


file = driver.find_element_by_xpath("/html/body/div[1]/section[1]/ul/li[20]")
file.click()
menu = driver.find_element_by_id("f9")
menu.click()
view = driver.find_element_by_xpath("/html/body/div[1]/ul[2]/li[1]")
view.click()
time.sleep(30)

driver.close()
