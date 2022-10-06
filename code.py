# import needed packages
import requests
from bs4 import BeautifulSoup
import pandas as pd

#####################################################################
# first webpage
page1 = requests.get('https://www.alz.org/news/2022')

# Create a BeautifulSoup object
soup1 = BeautifulSoup(page1.text, 'html.parser')

# print pretty
print(soup1.prettify())

# get names of each article listed in "Recent News"
head_name = soup1.find_all('h3',class_='card-title')
head_names = []
for n in head_name:
    name = n.text
    name = name.strip()
    name = name.replace('\n','')
    head_names.append(name)
len(head_names)

# get published date of each article listed in "Recent News"
foot_name =soup1.find_all('div',class_='card-footer')
foot_names = []
for f in foot_name:
    foot = f.text
    foot = foot.strip()
    foot = foot.replace('\n','')
    foot_names.append(foot)
len(foot_names)

# put these two pieces of information together into a dataframe
df1 = pd.DataFrame({'title':head_names,'date':foot_names})

df1.to_csv('data/web1.csv')

#####################################################################
# second webpage
page2 = requests.get('https://weather.com/weather/tenday/l/Long+Island+City+NY+USNY0833:1:US')

# Create a BeautifulSoup object
soup2 = BeautifulSoup(page2.text, 'html.parser')

# print pretty
print(soup2.prettify())

# get date for each day listed 
date = soup2.find_all('h3',class_='DetailsSummary--daypartName--2FBp2')
dates = []
for d in date:
    day = d.text
    day = day.strip()
    day = day.replace('\n','')
    dates.append(day)
len(dates)

# get lowest temp value for each day listed 
low_temp = soup2.find_all('span',attrs={'data-testid': 'lowTempValue'})
low_temps = []
for l in low_temp:
    templ = l.text
    templ = templ.strip()
    templ = templ.replace('\n','')
    low_temps.append(templ)
len(low_temps)

# get highest temp value for each day listed 
high_temp = soup2.find_all('span',attrs={'data-testid': 'TemperatureValue'},class_='DetailsSummary--highTempValue--3Oteu')
high_temps = []
for h in high_temp:
    temph = h.text
    temph = temph.strip()
    temph = temph.replace('\n','')
    high_temps.append(temph)
len(high_temps)

# get description for each day listed 
descrb = soup2.find_all('span',class_='DetailsSummary--extendedData--365A_')
descrbs = []
for de in descrb:
    description = de.text
    description = description.strip()
    description = description.replace('\n','')
    descrbs.append(description)
len(descrbs)

# put these pieces of information together into a dataframe
df2 = pd.DataFrame({'Date':dates,'Low_temp':low_temps,'High_temp':high_temps,'Description':descrbs})

df2.to_csv('data/web2.csv')