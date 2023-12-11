#import selenium web driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# WebDriver'ı başlat
driver = webdriver.Chrome()

# Web sayfasını aç
driver.get("https://www.akdeniz.edu.tr")

carousel = driver.find_element(By.ID, "carouselMain")
print(carousel)

# WebDriver'ı kapat
driver.quit()

