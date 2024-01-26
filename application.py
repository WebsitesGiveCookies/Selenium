from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from functions import login

robot_options = Options()
robot_options.add_experimental_option("detach",True)
robot = Chrome(options = robot_options)



login("mihai.ciorobitca@outlook.com","password123.", robot)
