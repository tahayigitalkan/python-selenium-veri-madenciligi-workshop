#import selenium web driver
from selenium import webdriver


# WebDriver'ı başlat
driver = webdriver.Chrome()

# Web sayfasını aç
driver.get("https://www.akdeniz.edu.tr")


# WebDriver'ı kapat
driver.quit()
