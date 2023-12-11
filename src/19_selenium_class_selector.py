#import selenium web driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# WebDriver'ı başlat
driver = webdriver.Chrome()

# Web sayfasını aç
driver.get("https://www.akdeniz.edu.tr")

site_links = driver.find_elements(By.CLASS_NAME, "site-map")

for site_link in site_links:
    print(site_link.text)

# WebDriver'ı kapat
driver.quit()
