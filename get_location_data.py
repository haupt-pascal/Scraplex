# import
import codecs
import json
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class WebDriver:
    location_data = {}

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.minimize_window()

        self.location_data["name"] = "NA"
        self.location_data["rating"] = "NA"
        self.location_data["location"] = "NA"
        self.location_data["data1"] = "NA"
        self.location_data["data2"] = "NA"
        self.location_data["data3"] = "NA"
        self.location_data["data4"] = "NA"
        self.location_data["data5"] = "NA"
        self.location_data["data6"] = "NA"
        self.location_data["data7"] = "NA"
        self.location_data["data8"] = "NA"
        self.location_data["url"] = url

    def company_scrape(self):
        time.sleep(15)
        try:
            name = self.driver.find_elements(By.TAG_NAME, value="h1")[0]
            location = self.driver.find_elements(By.CLASS_NAME, value="CsEnBe")[0]
            avg_rating = self.driver.find_element(By.CLASS_NAME, value="F7nice")
            data1 = self.driver.find_elements(By.CLASS_NAME, value="CsEnBe")[1]
            data2 = self.driver.find_elements(By.CLASS_NAME, value="CsEnBe")[2]
            data3 = self.driver.find_elements(By.CLASS_NAME, value="CsEnBe")[3]
            data4 = self.driver.find_elements(By.CLASS_NAME, value="CsEnBe")[4]
            data5 = self.driver.find_elements(By.CLASS_NAME, value="CsEnBe")[5]
            data6 = self.driver.find_elements(By.CLASS_NAME, value="CsEnBe")[6]
            data7 = self.driver.find_elements(By.CLASS_NAME, value="CsEnBe")[7]
            data8 = self.driver.find_elements(By.CLASS_NAME, value="CsEnBe")[8]
        except Exception as e:
            pass

        try:
            self.location_data["name"] = name.text
            self.location_data["location"] = location.text
            self.location_data["rating"] = avg_rating.text
            self.location_data["data1"] = data1.text
            self.location_data["data2"] = data2.text
            self.location_data["data3"] = data3.text
            self.location_data["data4"] = data4.text
            self.location_data["data5"] = data5.text
            self.location_data["data6"] = data6.text
            self.location_data["data7"] = data7.text
            self.location_data["data8"] = data8.text
            self.location_data["url"] = url
            self.build_json()
        except Exception as f:
            self.build_json()
            pass

    def build_json(self):
        try:
            with codecs.open('export.json', 'a', encoding='utf-8') as f:
                json.dump(self.location_data, f, ensure_ascii=False, sort_keys=False, indent=4)

        except Exception as e:
            with codecs.open('export.json', 'a', encoding='utf-8') as f:
                json.dump(self.location_data, f, ensure_ascii=False, sort_keys=False, indent=4)

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
file.close()
os.system('python json_encode.py')
