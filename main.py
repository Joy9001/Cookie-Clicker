import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

# Open a specific profile
option.add_argument(r"--user-data-dir=C:\Users\ASUS\AppData\Local\Google\Chrome\User Data")
option.add_argument(r"--profile-directory=Default")

driver = webdriver.Chrome(options=option)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")


def find_upgrades():
    upgrades = []

    cursor = driver.find_element(By.XPATH, '//*[@id="buyCursor"]')
    grandma = driver.find_element(By.XPATH, '//*[@id="buyGrandma"]')
    factory = driver.find_element(By.XPATH, '//*[@id="buyFactory"]')
    mine = driver.find_element(By.XPATH, '//*[@id="buyMine"]')
    shipment = driver.find_element(By.XPATH, '//*[@id="buyShipment"]')
    alchemy_lab = driver.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]')
    portal = driver.find_element(By.XPATH, '//*[@id="buyPortal"]')
    time_machine = driver.find_element(By.XPATH, '//*[@id="buyTime machine"]')

    upgrades.append(time_machine)
    upgrades.append(portal)
    upgrades.append(alchemy_lab)
    upgrades.append(shipment)
    upgrades.append(mine)
    upgrades.append(factory)
    upgrades.append(grandma)
    upgrades.append(cursor)

    return upgrades


end_time = time.time() + 60 * 1
rep_time = time.time() + 10

while time.time() <= end_time:
    cookie.click()

    if time.time() > rep_time:
        all_upgrades = find_upgrades()
        for ug in all_upgrades:
            if ug.get_attribute("class") != "grayed":
                ug.click()
                break
        rep_time = time.time() + 10
