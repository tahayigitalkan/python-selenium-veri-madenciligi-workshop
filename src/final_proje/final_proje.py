import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from researcher import Researcher

# WebDriver'ı başlat
driver = webdriver.Chrome()

# Web sayfasını aç
driver.get("https://akademik.yok.gov.tr/AkademikArama/view/universityListview.jsp")

# Belirli bir öğeyi bul
universities = driver.find_elements(By.CSS_SELECTOR,".searchable tr td:first-child a")

#tüm üniversiteleri yazdır
print("Üniversiteler:")
for university in universities:
    print(university.text)

#ilk üniversiteye tıkla
universities[0].send_keys(Keys.ENTER + Keys.RETURN)

#araştırmacıları bul
researchers = driver.find_elements(By.CSS_SELECTOR,"#authorlistTb > tbody > tr")
for researcher in researchers:
    print(researcher.text)

#ilk araştırmacı linkini bul
researcherLink = researchers[0].find_element(By.CSS_SELECTOR,"td:nth-child(3) > h4:nth-of-type(1) > a")
yok_id = researcherLink.get_attribute("href").split("=")[-1]

name = researcherLink.text
title = researcher.find_element(By.CSS_SELECTOR,"td:nth-child(3) > h6:nth-of-type(1)").text
department_tree = researcher.find_element(By.CSS_SELECTOR,"td:nth-child(3) > h6:nth-of-type(2)").text.split("/")

#araştırmacı nesnesini oluştur
researcher = Researcher(yok_id, name, title)
for department in department_tree:
    researcher.add_department(department)

with open('araştırmacılar.txt', 'w', encoding='utf8') as json_file:
    json.dump(researcher.__dict__, json_file, ensure_ascii=False)

# WebDriver'ı kapat
driver.quit()


#Ödev: Tüm üniversitelerin araştırmacılarını bulup, araştırmacılar.txt dosyasına kaydedin.