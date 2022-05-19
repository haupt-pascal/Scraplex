# import
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

        self.location_data["name"] = "NA"
        self.location_data["rating"] = "NA"
        self.location_data["location"] = "NA"
        self.location_data["data1"] = "NA"
        self.location_data["data2"] = "NA"
        self.location_data["data3"] = "NA"
        self.location_data["data4"] = "NA"
        self.location_data["url"] = url

    def company_scrape(self):
        time.sleep(15)
        try:
            name = self.driver.find_elements_by_tag_name("h1")[0]
            location = self.driver.find_elements_by_class_name('Io6YTe')[0]
            avg_rating = self.driver.find_element_by_class_name('F7nice')
            data1 = self.driver.find_elements_by_class_name('Io6YTe')[1]
            data2 = self.driver.find_elements_by_class_name('Io6YTe')[2]
            data3 = self.driver.find_elements_by_class_name('Io6YTe')[3]
            data4 = self.driver.find_elements_by_class_name('Io6YTe')[4]
        except Exception as e:
            print(e)
            pass

        try:
            self.location_data["name"] = name.text
            self.location_data["location"] = location.text
            self.location_data["rating"] = avg_rating.text
            self.location_data["data1"] = data1.text
            self.location_data["data2"] = data2.text
            self.location_data["data3"] = data3.text
            self.location_data["data4"] = data4.text
            self.location_data["url"] = url
            self.build_json()
        except Exception as f:
            print(f)
            self.build_json()
            pass

    def build_json(self):
        try:
            print(self.location_data, file=open('export.json', 'a', encoding="utf-8"))
        except Exception as e:
            print(e)
            print(self.location_data, file=open('export.json', 'a'))

    def scrape(self, url):
        try:
            self.driver.get(url)
        except Exception as e:
            self.driver.quit()
            pass
        #time.sleep(10)

        self.company_scrape()
        self.driver.quit()
        return (self.location_data)

file = open("links.txt", "r")
lines = file.readlines()
for line in lines:
    url = line
    x = WebDriver()
    print(x.scrape(url))
