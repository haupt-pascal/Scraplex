# import
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class WebDriver:
    location_data = {}

    def __init__(self):
        self.PATH = "chromedriver.exe"
        self.options = Options()
        # self.options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
        self.options.add_argument("--headless")
        self.options.add_argument("--enable-javascript")
        self.driver = webdriver.Chrome(self.PATH, options=self.options)
        #self.driver.maximize_window()

        self.location_data["rating"] = "NA"
        self.location_data["reviews_count"] = "NA"
        self.location_data["location"] = "NA"
        self.location_data["contact"] = "NA"
        self.location_data["website"] = "NA"
        self.location_data["Time"] = {"Monday": "NA", "Tuesday": "NA", "Wednesday": "NA", "Thursday": "NA",
                                      "Friday": "NA", "Saturday": "NA", "Sunday": "NA"}
        self.location_data["Reviews"] = []
        self.location_data["Popular Times"] = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [],
                                               "Friday": [], "Saturday": [], "Sunday": []}

    def page_scroll(self):
        print(' ')
        print('task is loading, sleeping for 3 seconds now')
        time.sleep(3)

        element = self.driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]')
        self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', element)
        print(' ')
        print('scrolling down')
        time.sleep(1)
        self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', element)
        time.sleep(1)
        self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', element)

    def open_next_page(self):
        button = self.driver.find_element_by_xpath('//*[@id="ppdPk-Ej1Yeb-LgbsSe-tJiF1e"]')
        button.click()

    def link_scrape(self):
        link_list = set()
        full_link_list = set()
        html = self.driver.page_source
        soup = BeautifulSoup(html, features="html.parser")

        for line in soup.find_all('a'):
            link = line.get('href')
            if not link:
                continue

            if link == "https://www.google.de/intl/de/about/products?tab=lh":
                continue

            if link == "https://support.google.com/maps/?hl=de&authuser=0&p=no_javascript":
                continue

            if link.startswith('https://accounts.google.com'):
                continue

            if link.startswith('http'):
                link_list.add(link)

            for link in link_list.union():
                if link in full_link_list:
                    continue
                else:
                    full_link_list.add(link)
                    print(link, file=open('links.txt', 'a'))

    def scrape(self, url):
        try:
            self.driver.get(url)
        except Exception as e:
            self.driver.quit()
            pass
        time.sleep(10)
        count = 0
        working = False
        while not working:
            try:
                working = True
                while count < int(input_count):
                    self.page_scroll()
                    self.link_scrape()
                    self.open_next_page()
                    count += 1
                    print("page " + str(count) + " is now finished...")

            except Exception:
                self.driver.close()
                print("task got some error, need to restart - don't worry, it'll be finished soon")
                self.__init__()
                self.scrape(url)
                pass

            if count == int(input_count):
                self.driver.quit()
                os.system('python get_location_data.py')


keyword = input('enter keyword of company you want to scrape: ')
input_count = input('enter amount of pages you want to scrape: ')
url = "https://www.google.de/maps/search/" + keyword
x = WebDriver()
print(x.scrape(url))