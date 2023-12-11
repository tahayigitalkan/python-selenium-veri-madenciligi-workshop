#import selenium web driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# WebDriver'ı başlat
driver = webdriver.Chrome()

# Web sayfasını aç
driver.get("https://www.akdeniz.edu.tr")

search_button = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-btn"))
)

search_button.send_keys(Keys.ENTER + Keys.RETURN)

txt_search = driver.find_element(By.ID,"txt_search")

txt_search.send_keys("Mühendislik" + Keys.ENTER + Keys.RETURN)

driver.quit()
