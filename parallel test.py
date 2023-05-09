import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


username = "gauravplambdatest"
access_key = "xNsKqBnq3R8179bmY9kiso6XY9Qf5CiQLwcxWU9NbtWf2pp86R"

grid_Url = "hub.lambdatest.com/wd/hub"

ch_capabilities = {
    'LT:Options': {
        "build": "test1",
        "name": "Gaurav",
        "platformName": "Windows 11",
    },
    "browserName": "Chrome",
    "browserVersion": "latest",

}
# Edge_capabilities = {
#     'LT:Options': {
#         "build": "test1",
#         "name": "Gaurav",
#         "platformName": "Windows 11",
#     },
#     "browserName": "MicrosoftEdge",
#     "browserVersion": "latest",
#
#
#     }

url = "https://"+username+":"+access_key+"@"+grid_Url

driver = webdriver.Remote(
    command_executor=url,
    desired_capabilities=ch_capabilities

    )

# driver1 = webdriver.Remote(
#     command_executor=url,
#     desired_capabilities=Edge_capabilities
#     )
driver.get("https://accounts.lambdatest.com/")
# driver.get("https://accounts.lambdatest.com/")

u_name = driver.find_element("id", "email")
u_name.send_keys("gauravp@lambdatest.com")
# uname.send_keys("gauravp@lambdatest.com")

# for  password
p_word = driver.find_element("id", "password")
p_word.send_keys("G@urav030895")

# for login
login = driver.find_element("id", "login-button")
login.send_keys(Keys.ENTER)

time.sleep(10)

# for dropdown
driver.find_element(By.XPATH, "//*[@id='profile__dropdown__parent']").click()
driver.find_element(By.XPATH, "//*[@id='item__manage__team']").click()

# for downloading file
driver.find_element(By.XPATH, "//*[@id='app']/section/div/div/div[2]/div[2]/div[1]/div[2]/div/div[1]").click()
driver.find_element(By.XPATH, "//*[@id='app']/section/div/div/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[2]").click()

# for Redirecting to the upload file page

driver.get("https://cgi-lib.berkeley.edu/ex/perl5/fup.html")

# for uploading the csv file

upload_csv = driver.find_element(By.XPATH, "/html/body/form/input[1]")

# FOR Browse the file from the system

upload_csv.send_keys("C:/Users/gauravp/Downloads/Invited Users.csv")

# for uploading the file
press = driver.find_element(By.XPATH, "/html/body/form/input[3]")
press.click()

print("Test completed")

time.sleep(10)
driver.quit()
