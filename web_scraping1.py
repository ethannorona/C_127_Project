from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

bright_starts_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(bright_starts_url)
print(page)

soup = bs(page.text, 'html.parser')
star_table = soup.find('table')

temp_list = []
table_rows = star_table.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)
    
Names = []
Distance = []
Mass = []
Radius = []
Luminosity = []

for i in range(1, len(temp_list)):
    Names.append(temp_list[i][1])
    Distance.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])
    Luminosity.append(temp_list[i][7])
    
dataframe2 = pd.DataFrame(list(zip(Names, Distance, Mass, Radius, Luminosity)), colums = ['Name', 'Distance', 'Mass', 'Radius', 'Luminosity'])
print(dataframe2)

dataframe2.to_csv('bright_starts.csv')