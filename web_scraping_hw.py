from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(start_url)

soup = BeautifulSoup(page.text, "html.parser")

star_table = soup.find('table')

temp_list = []
rows = star_table.find_all('tr')

for tr in rows:
      td = tr.find_all('td')
      row = [i.text.rstrip() for i in td]
      temp_list.append(row)

name = []
dist = []
mass = []
radius = []
luminous = []

for i in range(1, len(temp_list)):
      name.append(temp_list[i][1])
      dist.append(temp_list[i][3])
      mass.append(temp_list[i][5])
      radius.append(temp_list[i][6])
      luminous.append(temp_list[i][7])

df2 = pd.DataFrame(list(zip(name,dist,mass,radius,luminous)),columns=['Star_name','Distance','Mass','Radius','Luminosity'])

df2.to_csv("final_output.csv")