#from operator import div
#import projects as projects
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\Sushmitha\\Documents\\drivers\\chromedriver_win32\\chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://www.d3a.io/")
driver.maximize_window()
print(driver.title)
driver.find_element(By.CLASS_NAME, 'button__label').click()


#Validate that a existing user is able to login to d3a.io

driver.find_element(By.ID, 'email').send_keys("sushmithanraj@gmail.com")
driver.find_element(By.ID, 'password').send_keys("Tester@123")
driver.find_element(By.CLASS_NAME, 'button__label').click()

time.sleep(3)
print("testcase1 is successfully completed")
#creating a project

driver.find_element(By.XPATH, "html/body/div/div/div/nav/div[2]/div/div[2]/div/div/button").click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/header/div[3]/button[2]').click()
driver.find_elements(By.CSS_SELECTOR, "body > div:nth-child(11) > div > div")

#driver.switch_to.window(driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(11) > div > div")).send_keys
driver.find_element(By.ID, "input-field-name").send_keys("testa")
driver.find_element(By.NAME, "nameTextArea").send_keys("For testing purpose")
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[2]/button").click()
time.sleep(3)
print("testcase2 is successfully completed")

#validating the project listing after created
driver.find_elements(By.CSS_SELECTOR, "#root > div > div.Pane.vertical.Pane2.js-Pane2.Pane2--projects > div.route-transition-wrapper > div > div > section")
if driver.page_source.__contains__("testa"):
    print("Created project name is present")
else:
    print("Created project is absent")

#create a simulation in the project
driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div')
driver.find_element(By.CSS_SELECTOR, "#root > div > div.Pane.vertical.Pane2.js-Pane2.Pane2--projects > div.route-transition-wrapper > div > div > section > div:nth-child(1) > div > div.saved-project__headline > span > div > div > svg").click()
driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/section/div[1]/div[2]/button').click()
driver.find_element(By.XPATH, '//*[@id="input-field-name"]').clear()
time.sleep(2)
driver.find_element(By.ID, 'input-field-name').send_keys("Test_Simulator")
driver.find_element(By.ID, 'textarea-field-description').send_keys("Test_Simulator_Description")
driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/button').click()
time.sleep(3)


#check for the listing is proper

driver.find_element(By.XPATH, "html/body/div/div/div/nav/div[2]/div/div[2]/div/div/button").click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div')
time.sleep(2)
if driver.page_source.__contains__("simulationTest_Simu"):
    print("Created simulator is present")
else:
    print("Created simulator is absent")


driver.quit()
