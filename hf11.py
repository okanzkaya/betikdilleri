import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
class Eksi:
    def __init__(self, link, driver):
        self.link_listesi = []
        self.driver = driver
        self.link = link
        self.url = "https://eksisozluk.com/basliklar/gundem"
    def tamekran_yap(self):
        self.driver.maximize_window()
    def icerigi_cek(self, url):
        self.driver.get(url)
        wait = WebDriverWait(self.driver, 60)
        container = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".topic-list.partial")))
        time.sleep(5)
        li = container.find_elements(By.TAG_NAME, "li")

        for i in li:
            try:
                a = i.find_element(By.TAG_NAME, 'a')
                link = a.get_attribute('href')
                self.link_listesi.append(link)
            except:
                continue
        daha_fazla = self.driver.find_element(By.ID, "quick-index-continue-link")
        self.driver.execute_script("arguments[0].click();", daha_fazla)

        time.sleep(5)
        container1 = self.driver.find_element(By.CSS_SELECTOR, ".topic-list.partial")
        li1 = container1.find_elements(By.TAG_NAME, "li")

        for j in li1:
            try:
                a1 = j.find_element(By.TAG_NAME, 'a')
                link1 = a1.get_attribute('href')
                self.link_listesi.append(link1)
            except:
                continue
        # 3. part

        son = self.driver.find_element(By.CLASS_NAME, "last")
        self.driver.execute_script("arguments[0].click();", son)

        time.sleep(5)
        container1 = self.driver.find_element(By.CSS_SELECTOR, ".topic-list.partial")
        li2 = container1.find_elements(By.TAG_NAME, "li")

        for k in li2:
            try:
                a2 = k.find_element(By.TAG_NAME, 'a')
                link2 = a2.get_attribute('href')
                self.link_listesi.append(link2)
            except:
                continue
        return link_listesi
    def txtyeyazdir(self):
        for k in self.link_listesi():
            dosya = open(f'{k}.txt', 'w')
            with open(dosya, "w") as f:
                f.write(k)
    def main(self):
        self.tamekran_yap()
        link_listesi = self.icerigi_cek(self.url)
        print(link_listesi)
        self.txtyeyazdir()

url = "https://eksisozluk.com/basliklar/gundem"
driver = webdriver.Chrome()
test = Eksi(url, driver)
test.main()
