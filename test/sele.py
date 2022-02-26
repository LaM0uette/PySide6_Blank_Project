import threading
import time

from selenium import webdriver
from selenium.webdriver import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.touch_actions import TouchActions


options = Options()
options.add_argument(r"user-data-dir=C:\Users\XD5965\AppData\Local\Google\Chrome\User Data\Default")
# options.add_argument("--headless")
# options.add_argument("--disable-gpu")
driver = webdriver.Chrome(executable_path=r'C:\Users\XD5965\Creative Cloud Files\01_PROJETS\01_PROG\01_PYTHON\PySide6_Blank_Project_demo\test\chromedriver.exe', chrome_options=options)

lien = "https://github.com/sommerc/pyqt-stylesheets/blob/master/pyqtcss/src/dark_blue/style.qss"
driver.get(lien)
time.sleep(4)

print("Scroll")

element = driver.find_element_by_id("js-repo-pjax-container")

driver.execute_script("arguments[0].scrollIntoView(true);", element)
driver.execute_script("window.scrollBy(0, 150);")


"""
scroll vers le bas :
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

boucle sur elements avec xpatj
elem = driver.find_elements_by_xpath("//div[@class='']/img")
for items in elem:
    src = items.get_attribute('src')
    lst.add(src)

click
element = driver.find_element(By.XPATH, "//button[@class='']")
    element.click()

touche
elem.send_keys(Keys.RETURN)
"""
def FUNC():
    pass

TH = threading.Thread(target=FUNC)
TH.start()
