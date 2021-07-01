from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs4
import time

class JobCan:
    #コンストラクタ
    def __init__(self):
        self.options = Options()
        self.options.add_argument('--headless')
        self.options.add_argument('--window-size=1920,1080')
        self.driver = webdriver.Chrome(options=self.options)

    #webページを開く
    def open_url(self, url):
        self.driver.get(url)

    def click_page(self, sleep_seconds = 0):
        #ログイン
        self.driver.find_element_by_name('user[email]').send_keys('takafumi.aoki@2-ward.com')
        self.driver.find_element_by_name('user[password]').send_keys('jbHello2ward@')
        self.driver.find_element_by_css_selector('.form__login').click()
        time.sleep(sleep_seconds)
    #勤怠画面へ移動
    self.driver.find_element_by_css_selector('.jbc-app-link').click()
    time.sleep(sleep_seconds)
    #ページソースをUTF-8にエンコードして取得し、ブラウザを閉じる
    self.data = self.driver.page_source.encode('utf-8')
    self.driver.save_screenshot('my_page.png')
    self.driver.quit()

#スクレイピング
    def scrape_page(self):
        html = bs4(self.data, 'html.parser')
        mistakes = html.select('#top_info_area tr')
        print(mistakes)

if __name__ == '__main__':
    driver = JobCan()
    driver.open_url('https://ssl.jobcan.jp/login/pc-employee/')
    driver.click_page(sleep_seconds = 3)
    driver.scrape_page()"
