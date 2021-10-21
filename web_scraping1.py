from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("C://Users/ethan/OneDrive/Desktop/WH Jr. Projects/Python Programming/C 127 Project/chromedriver.exe")
browser.get(START_URL)
time.sleep(10)

def scrape():
    headers = ["Name", "Distance", "Mass", "Radius"]
    star_data = []
    soup = BeautifulSoup(browser.page_source, "html.passer")
    for tr_tag in soup.find_all("tr"):
        td_tags = tr_tag.find_all("td")
        temp_list = []
        for index, td_tag in enumerate(td_tags):
            if index == 0:
                temp_list.append(td_tag.find_all("a")[0].contents[0])
            else:
                try:
                    temp_list.append(td_tag.contents[0])
                except:
                    temp_list.append("")
            star_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="mw-normal-catlinks"]/ul/li[1]/a').click
    with open("scraper_2.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(star_data)

scrape()